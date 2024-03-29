<template>
  <div :class="[$style.eventBox, $style[$mq]]">
    <div :class="$style.title">
      <span :class="$style.txt">{{ getTitle }}</span>
      <span :class="$style.txt2">
        <router-link :to="getPath">View Details</router-link>
      </span>
    </div>
    <BounceLoader :loading="loading" color="#E47718" :class="$style.loader" />
    <div
      :class="$style.registerWrapper"
      v-if="showRegistration"
      v-show="!loading"
    >
      <div v-if="!isRegOn" v-show="!isEventManthan" :class="$style.orBox">
        <span>Registration Closed</span>
      </div>
      <div v-if="isRegOn" :class="$style.btnBox">
        <button :class="$style.btn" @click="displayBtnClick" :data-input-target="`${event.name}__teamName`"
          :id="`${event.name}__createTeam`" v-show="!isEventManthan">
          Create Team/Participate Individually
        </button>
        <button :class="$style.btn" @click="displayBtnClick" :data-input-target="`${event.name}__teamName`"
          :id="`${event.name}__createTeam`" v-show="isEventManthan">
          Participate Individually
        </button>
        <div v-if="isRegOn" :class="$style.behindBtn">
          <input type="text" :class="[$style.field]" placeholder="Team Name" @keyup="collectInput"
            :data-button-target="`${event.name}__createTeam`" v-model="teamName" :id="`${event.name}__teamName`"
            v-show="!isEventManthan" />
          <input type="text" :class="[$style.field]" placeholder="Your Name" @keyup="collectInput"
            :data-button-target="`${event.name}__createTeam`" v-model="teamName" :id="`${event.name}__teamName`"
            v-show="isEventManthan" />
          <button value=">" :class="$style.submit" :data-event-id="event.id" @click="submitCreateTeam">
            <i class="fas fa-arrow-circle-right"></i>
          </button>
        </div>
      </div>
      <div v-if="isRegOn" v-show="!isEventManthan" :class="$style.orBox">
        <span>OR</span>
      </div>
      <div v-if="isRegOn" v-show="!isEventManthan" :class="$style.btnBox">
        <button :class="$style.btn" @click="displayBtnClick" :data-input-target="`${event.name}__accessCode`"
          :id="`${event.name}__joinTeam`">
          Join Team
        </button>
        <div :class="$style.behindBtn">
          <input type="text" :class="[$style.field]" :data-button-target="`${event.name}__joinTeam`"
            placeholder="Access Code" v-model="accessCode" @keyup="collectInput" :id="`${event.name}__accessCode`" />
          <button value=">" :class="$style.submit" :data-event-id="event.id" @click="submitJoinTeam">
            <i class="fas fa-arrow-circle-right"></i>
          </button>
        </div>
      </div>
    </div>
    <div :class="$style.teamWrapper" v-else v-show="!loading">
      <div :class="$style.teamHeader">
        <h3>
          {{ team.name }}
          <span class="fas fa-circle" :class="isTeamValid ? $style.validTeam : $style.invalidTeam"
            :title="teamInfo"></span>
        </h3>
        <div :class="$style.infoBox" v-show="!isTeamFull">
          <span v-show="!isEventManthan" :class="$style.key">Access Code:</span>
          <span :class="$style.value">{{ team.access_code }}</span>
          <i class="fas fa-clipboard" :class="$style.copyIcon" @click="clickToCopy"></i>
        </div>
      </div>
      <div :class="$style.memberList">
        <ul>
          <li :class="$style.teamMember" v-for="(member, i) in teamMembers" :key="i">
            {{ member.name }}
            <i class="fas fa-times" :class="$style.removeIcon" :data-member-id="member.id" :data-index="i"
              @click="deleteMember" v-if="isTeamLeader"></i>
          </li>
        </ul>
      </div>
      <button :class="$style.teamLeave" @click="leaveTeam">
        {{ isTeamLeader ? (isEventManthan ? "Delete Registration" : "Delete Team") : "Leave Team" }}
      </button>
      <div :class="$style.teamInfo" v-if="!isTeamValid">* {{ teamInfo }}</div>
    </div>
  </div>
</template>

<script>
import { copyToClipboard } from "@js/utils";
import eventsStore from "@store/events";
import { BounceLoader } from "@saeris/vue-spinners";
import API from "@js/api";
export default {
  components: {
    BounceLoader,
  },
  data() {
    return {
      teamName: "",
      accessCode: "",
      loading: false,
      isRegOn: false,
    };
  },
  props: {
    event: {
      type: Object,
      required: true,
    },
  },
  computed: {
    isEventManthan() {
      let event_id = this.event.id
      if(!event_id) event_id = this.$route.params.id;
      return event_id == 4;
    },
    showRegistration() {
      return !this.team;
    },
    team() {
      return this.event.team;
    },
    teamMembers() {
      return this.team.members;
    },
    isTeamLeader() {
      return this.team.creator;
    },
    isTeamValid() {
      return !this.isTeamMissingMembers;
    },
    isTeamMissingMembers() {
      return this.teamMembers.length < this.event.min_members;
    },
    isTeamFull() {
      return this.teamMembers.length === this.event.max_members;
    },
    teamInfo() {
      if (this.isTeamMissingMembers)
        return `Missing ${this.event.min_members -
          this.teamMembers.length} members.`;
    },
    getPath() {
      return `/events-timeline/${this.event.id}`
    },
    getTitle() {
      const event = eventsStore.events.find(e => e.name === this.event.name)
      if (event) return event.title
      return ""
    }
  },
  methods: {
    closeOtherButtons(btn, clickedBtn) {
      if (btn && btn !== clickedBtn) {
        btn.style.animation = "none";
        btn.classList.remove(this.$style.animateHideBtn);
        // Trigger reflow of element to restart CSS animation (source: https://stackoverflow.com/a/45036752/10623486)
        btn.offsetWidth;
        btn.style.animation = null;
      }
    },
    displayBtnClick(e) {
      const { target: btn } = e;
      const inputId = btn.getAttribute("data-input-target");
      btn.style.animation = "none";
      document.getElementById(inputId).focus();
      btn.classList.add(this.$style.animateHideBtn);
      // Trigger reflow of element to restart CSS animation (source: https://stackoverflow.com/a/45036752/10623486)
      btn.offsetWidth;
      btn.style.animation = null;
      eventsStore.events.forEach((event) => {
        const createTeamBtn = document.getElementById(`${event.name}__createTeam`);
        const joinTeamBtn = document.getElementById(`${event.name}__joinTeam`);
        this.closeOtherButtons(createTeamBtn, btn);
        this.closeOtherButtons(joinTeamBtn, btn);
      })
    },
    collectInput(e) {
      if (e.keyCode == 13) {
        // Enter is pressed.
        const { id } = e.target;
        if (id === `${this.event.name}__teamName`)
          return this.submitCreateTeam();
        else return this.submitJoinTeam();
      }
    },
    submitCreateTeam() {
      this.startLoading();
      this.$store
        .dispatch("createEventTeam", {
          eventId: this.event.id,
          teamName: this.teamName,
        })
        .then(({ data }) => {
          this.stopLoading();
          this.event.team = data;
        })
        .catch((err) => {
          this.stopLoading();
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    submitJoinTeam() {
      this.startLoading();
      this.$store
        .dispatch("joinEventTeam", { accessCode: this.accessCode })
        .then(({ data }) => {
          this.stopLoading();
          this.event.team = data;
        })
        .catch((err) => {
          this.stopLoading();
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    deleteMember(e) {
      this.startLoading();
      const memberId = e.target.getAttribute("data-member-id");
      const memberIndex = e.target.getAttribute("data-index");
      this.$store
        .dispatch("removeMemberFromTeam", {
          teamId: this.team.id,
          memberId,
        })
        .then((_) => {
          this.stopLoading();
          this.teamMembers.splice(memberIndex, 1);
        })
        .catch((err) => {
          this.stopLoading();
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    clickToCopy(e) {
      const accessCode = this.team.access_code;
      copyToClipboard(accessCode);
      this.$toasted.global.success({ message: `Copied "${accessCode}"!` });
    },
    leaveTeam(e) {
      this.startLoading();
      this.$store
        .dispatch("leaveTeam", { teamId: this.team.id })
        .then((_) => {
          this.stopLoading();
          this.event.team = null;
        })
        .catch((err) => {
          this.stopLoading();
          this.$toasted.global.error_post({ message: err.message });
        });
    },
    startLoading() {
      this.loadingTime = Math.trunc(new Date().getTime() / 1000);
      this._startLoading();
    },
    stopLoading() {
      const timeDiff =
        Math.trunc(new Date().getTime() / 1000) - this.loadingTime;
      if (timeDiff >= 1000) _stopLoading();
      else setTimeout(this._stopLoading.bind(this), 1000 - timeDiff);
    },
    _startLoading() {
      this.loading = true;
    },
    _stopLoading() {
      this.loading = false;
    },
  },
  created() {
    let event_id = this.event.id
    if(!event_id) event_id = this.$route.params.id;
    API.fetch(`events/${event_id}/`)
      .then(({ data }) => {
        this.isRegOn = data.is_registration_on
      })
      .catch(console.log)
  },
  mounted() {
    document
      .querySelectorAll(`.${this.$style.btn}`)
      .forEach((elem) => (elem.style.animation = "none"));
  },
};
</script>
<style module lang="stylus">
$box-large-width = 350px;
$box-small-width = 280px;
$btn-width = 240px;

@keyframes animate {
  0% {
    opacity: 1;
    transform: translateX(0px);
  }

  100% {
    opacity: 0;
    transform: translateX(-300px);
  }
}

.eventBox {
  --event-team-box-width: $box-large-width;
  --event-team-button-width: $btn-width;
  width: 70vw;
  max-width: 700px;
  height: 400px;
  padding: 10px 20px 40px;
  box-shadow: var(--box-shadow);
  background-color: var(--background-color);
  border-radius: 0 30px;
  margin: 40px 0px; 

  &.xs, &.sm {
    --event-team-box-width: $box-small-width;
  }

  .loader {
    margin: 20px auto 50px;
    padding: 5px;
  }

  .title {
    height: 70px;
    margin-bottom: 50px;

    .txt {
      $font-size: 30px;
      font-family: 'Baloo Bhaina 2';
      text-align: center;
    }

    .txt2 {
      float: right;
      font-weight: 700;
      $font-size: 25px;
    }
  }

  .btnBox {
    height: 60px;
    position: relative;
    text-align: center;
    width: 60vw;
    max-width: 500px;
    margin: 20px auto;
  }

  .btn {
    position: absolute;
    z-index: 5;
    width: 100%;
    top: 0;
    left: 0;
    background-color: var(--background-color);
    box-shadow: var(--small-icon-shadow);
    color: $waterloo;
    font-family: 'Roboto Slab';
    padding: 10px;
    $font-size: 20px;
    border: none;
    border-radius: 5px;
    width: 100%;
    height: 100%;

    &:hover {
      box-shadow: var(--inset-small-icon-shadow);
      color: var(--text-color);
    }
  }

  .orBox {
    text-align: center;
    display: table;
    width: 100%;
    margin: 10px;
    font-family: QuickSand;
    font-size: 25px;

    span {
      display: table-cell;
      vertical-align: middle;
    }
  }

  .field {
    padding: 5px;
    clear: both;
    height: 40px;
    border: 0;
    outline: 0;
    width: calc(100% - 50px);
    color: var(--text-color);
    box-shadow: var(--inset-box-shadow);
    background-color: var(--background-color);
    $font-size: 16px;
    background: #fff2;
    border-radius: 5px;
  }

  .submit {
    border: 0;
    background: transparent;
    color: var(--text-color);
    border-radius: 100%;
    $font-size: 28px;
    height: 40px;
    width: 40px;
    cursor: pointer;
    text-align: center;

    &:hover {
      color: $vermilion;
    }
  }

  .behindBtn {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0
    z-index: 4;
  }

  .animateHideBtn {
    animation: animate 0.8s forwards;
    cursor: default;
  }

  .noAnimate {
    animation: none;
  }

  .teamWrapper {
    margin: 5px 20px;

    .teamHeader {
      text-align: center;

      .validTeam {
        color: $vermilion;
      }

      .invalidTeam {
        color: red;
      }
    }

    .memberList {
      ul {
        list-style: none;
      }

      .teamMember {
        margin-bottom: 5px;
        vertical-align: middle;

        .removeIcon {
          color: red;
          float: right;
          visibility: hidden;
          cursor: pointer;
        }

        &:hover .removeIcon {
          visibility: visible;
        }
      }
    }

    .teamInfo {
      $font-size: 18px;
      text-align: center;
    }

    .teamLeave {
      display: block;
      background: red;
      margin: 0 auto 5px;
      color: $white;
      padding: 5px 15px;
      border: none;
      border-radius: 10px;
    }
  }

  .infoBox {
    border: 2px solid $vermilion;
    border-radius: 10px;
    height: 40px;
    text-align: center;
    vertical-align: middle;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      $font-size: 16px;
    }

    .key {
      display: inline-block;
      vertical-align: middle;
      float: left;
      border-radius: inherit;
      border-bottom-right-radius: 0;
      border-top-right-radius: 0;
      border-right: 1px solid $vermilion;
      background: alpha($vermilion, 0.7);
      height: 100%;
      padding: 5px;
    }

    .value {
      display: inline-block;
      padding: 5px;
      height: 100%;
    }
  }

  .copyIcon {
    cursor: pointer;
    margin-right: 10px;
    margin-top: 10px;
    float: right;
  }
}
</style>
