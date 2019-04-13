<template>
  <div>
    <div :class="$style.registerBox">
      <div :class="$style.title">
        <span :class="$style.txt">{{ eventTitle }}</span>
        <span :class="$style.txt2">
          <a :href="eventLink">View Details</a>
        </span>
      </div>
      <div :class="$style.btnBox">
        <button
          :class="$style.btn"
          @click="displayBtnClick"
          :data-btn="`#${eventTitle}__teamName`"
          :id="`#${eventTitle}__createTeam`"
        >Create Team</button>
        <div :class="$style.behindBtn">
          <input
            type="text"
            :class="[$style.field]"
            placeholder="Team Name"
            @blur="inputBtnBlur"
            :data-input="`#${eventTitle}__createTeam`"
            v-model="teamName"
            :id="`#${eventTitle}__teamName`"
          >
          <button value=">" :class="[$style.submit]">
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
          :data-btn="`#${eventTitle}__accessCode`"
          :id="`#${eventTitle}__joinTeam`"
        >Join Team</button>
        <div :class="$style.behindBtn">
          <input
            type="text"
            :class="[$style.field]"
            :data-input="`#${eventTitle}__joinTeam`"
            placeholder="Access Code"
            v-model="accessCode"
            @blur="inputBtnBlur"
            :id="`#${eventTitle}__accessCode`"
          >
          <button value=">" :class="[$style.submit]">
            <i class="fas fa-arrow-circle-right"></i>
          </button>
        </div>
      </div>
    </div>
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
  props: ["eventTitle", "eventLink"],
  computed: {},
  methods: {
    displayBtnClick(e) {
      const { target: btn } = e;
      const inputId = btn.getAttribute("data-btn");
      btn.style.animation = "none";
      document.getElementById(inputId).focus();
      btn.classList.add(this.$style.animateHideBtn);
      // Trigger reflow of element to restart CSS animation (source: https://stackoverflow.com/a/45036752/10623486)
      btn.offsetWidth;
      btn.style.animation = null;
    },
    inputBtnBlur(e) {
      const btnId = e.target.getAttribute("data-input");

      const btn = document.getElementById(btnId);
      btn.style.animation = "none";
      btn.classList.remove(this.$style.animateHideBtn);
      // Trigger reflow of element to restart CSS animation (source: https://stackoverflow.com/a/45036752/10623486)
      btn.offsetWidth;
      btn.style.animation = null;
    }
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

$box-height = 250px;
$box-width = 350px;
$btn-width = 240px;

.registerBox {
  height: $box-height;
  width: $box-width;
  border: 1px solid $chartreuse;
}

.title {
  height: 50px;
  padding-top: 7px;

  .txt {
    font-size: 23px;
    margin-left: 7px;
    font-family: 'Aldo the Apache';
  }

  .txt2 {
    float: right;
    margin-right: 7px;
  }
}

.btnBox {
  height: 50px;
  position: relative;
  text-align: center;
  /* height: 60px; */
  width: $btn-width;
}

.btn {
  position: absolute;
  z-index: 5;
  width: 100%;
  top: 0;
  left: (($box-width - $btn-width) / 2);
  /*  */
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
  max-width: ($btn-width - 50px);
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
  left: (($box-width - $btn-width) / 2);
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
