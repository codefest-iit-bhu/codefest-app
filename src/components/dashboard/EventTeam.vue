<template>
  <div :class="[$style.eventBox, $style[$mq]]">
    <div :class="$style.title">
      <span :class="$style.txt">{{ event.title }}</span>
      <span :class="$style.txt2">
        <router-link :to="event.link">View Details</router-link>
      </span>
    </div>
    <div :class="$style.registerWrapper" v-if="showRegistration">
      <div :class="$style.btnBox">
        <button
          :class="$style.btn"
          @click="displayBtnClick"
          :data-input-target="`#${event.name}__teamName`"
          :id="`#${event.name}__createTeam`"
        >Create Team</button>
        <div :class="$style.behindBtn">
          <input
            type="text"
            :class="[$style.field]"
            placeholder="Team Name"
            @blur="inputBtnBlur"
            :data-button-target="`#${event.name}__createTeam`"
            v-model="teamName"
            :id="`#${event.name}__teamName`"
          >
          <button
            value=">"
            :class="$style.submit"
            :data-event-id="event.id"
            @click="submitCreateTeam"
          >
            <i class="fas fa-arrow-circle-right"></i>
          </button>
        </div>
      </div>
      <div :class="$style.orBox">
        <span>OR</span>
      </div>
      <div :class="$style.btnBox">
        <button
          :class="$style.btn"
          @click="displayBtnClick"
          :data-input-target="`#${event.name}__accessCode`"
          :id="`#${event.name}__joinTeam`"
        >Join Team</button>
        <div :class="$style.behindBtn">
          <input
            type="text"
            :class="[$style.field]"
            :data-button-target="`#${event.name}__joinTeam`"
            placeholder="Access Code"
            v-model="accessCode"
            @blur="inputBtnBlur"
            :id="`#${event.name}__accessCode`"
          >
          <button
            value=">"
            :class="$style.submit"
            :data-event-id="event.id"
            @click="submitJoinTeam"
          >
            <i class="fas fa-arrow-circle-right"></i>
          </button>
        </div>
      </div>
    </div>
    <div :class="$style.teamWrapper" v-else>Team</div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      teamName: "",
      accessCode: ""
    };
  },
  props: {
    event: {
      type: Object,
      required: true
    }
  },
  computed: {
    showRegistration() {
      return !this.event.team;
    }
  },
  methods: {
    displayBtnClick(e) {
      const { target: btn } = e;
      const inputId = btn.getAttribute("data-input-target");
      btn.style.animation = "none";
      document.getElementById(inputId).focus();
      btn.classList.add(this.$style.animateHideBtn);
      // Trigger reflow of element to restart CSS animation (source: https://stackoverflow.com/a/45036752/10623486)
      btn.offsetWidth;
      btn.style.animation = null;
    },
    inputBtnBlur(e) {
      const btnId = e.target.getAttribute("data-button-target");

      const btn = document.getElementById(btnId);
      btn.style.animation = "none";
      btn.classList.remove(this.$style.animateHideBtn);
      // Trigger reflow of element to restart CSS animation (source: https://stackoverflow.com/a/45036752/10623486)
      btn.offsetWidth;
      btn.style.animation = null;
    },
    submitCreateTeam() {
      this.$store.dispatch("createEventTeam");
    },
    submitJoinTeam() {}
  },
  mounted() {
    document
      .querySelectorAll(`.${this.$style.btn}`)
      .forEach(elem => (elem.style.animation = "none"));
  }
};
</script>
<style module lang = "stylus" >
@require '~@styles/theme';

$box-large-width = 350px;
$box-small-width = 280px;
$btn-width = 240px;

.eventBox {
  --event-team-box-width: $box-large-width;
  --event-team-button-width: $btn-width;
  width: var(--event-team-box-width);
  padding: 10px 10px 20px;
  border: 1px solid $chartreuse;

  &.xs, &.sm {
    --event-team-box-width: $box-small-width;
  }
}

.title {
  height: 50px;

  .txt {
    font-size: 23px;
    font-family: 'Aldo the Apache';
  }

  .txt2 {
    float: right;
  }
}

.btnBox {
  height: 50px;
  position: relative;
  text-align: center;
  width: var(--event-team-button-width);
}

.btn {
  position: absolute;
  z-index: 5;
  width: 100%;
  top: 0;
  left: calc(((var(--event-team-box-width) - var(--event-team-button-width)) / 2));
  background-color: black;
  border: 1px solid $chartreuse;
  color: $chartreuse;
  font-family: 'Aldo the Apache';
  padding: 15px;
  font-size: 20px;
  border-radius: 5px;
  width: inherit;
  animation: animate 0.5s reverse;

  &:hover {
    box-shadow: inset 0px 0px 7px #86ff00;
  }
}

.orBox {
  text-align: center;
  display: table;
  width: 100%;
  margin: 10px;
  height: 40px;
  font-family: QuickSand;

  span {
    display: table-cell;
    vertical-align: middle;
  }
}

.field {
  padding: 5px;
  clear: both;
  height: 30px;
  color: white;
  border: 0;
  outline: 0;
  max-width: calc(var(--event-team-button-width) - 50px);
  font-size: 16px;
  background: #fff2;
  border-radius: 5px;
}

.submit {
  border: 0;
  background: transparent;
  color: $white;
  border-radius: 100%;
  font-size: 22px;
  height: 40px;
  width: 40px;
  cursor: pointer;
  text-align: center;

  &:hover {
    color: $chartreuse;
  }
}

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

.behindBtn {
  position: absolute;
  width: 100%;
  top: 0;
  left: calc(((var(--event-team-box-width) - var(--event-team-button-width)) / 2));
  z-index: 4;
}

.animateHideBtn {
  animation: animate 0.8s forwards;
  cursor: default;
}

.noAnimate {
  animation: none;
}
</style>
