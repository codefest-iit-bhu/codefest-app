<template>
  <div style="margin-left:30px;">
    <br>
    <br>
    <div :class="$style.registerBox">
      <div :class="$style.title">
        <span :class="$style.txt">{{eventTitle}}</span>
        <span :class="$style.txt2">View Details</span>
      </div>
      <div :class="$style.btnBox">
        <table style="height:100%;width:100%;">
          <tr>
            <td>
              <center>
                <button :class="[$style.btn1,btn1clicked]" @click="btn1click = true">Create Team</button>
                <input
                  type="text"
                  :class="[$style.field,input1clicked]"
                  placeholder="Team Name"
                  v-model="input1"
                >
                <button value=">" :class="[$style.submit,input1clicked]">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </center>
            </td>
          </tr>
        </table>
      </div>
      <div :class="$style.orBox">
        <table style="height:100%;width:100%;">
          <tr>
            <td>
              <center>OR</center>
            </td>
          </tr>
        </table>
      </div>
      <div :class="$style.btnBox">
        <table style="height:100%;width:100%;">
          <tr>
            <td>
              <center>
                <button :class="[$style.btn2,btn2clicked]" @click="btn2click = true">Join Team</button>
                <input
                  type="text"
                  :class="[$style.field,input2clicked]"
                  placeholder="Access Code"
                  v-model="input2"
                >
                <button value=">" :class="[$style.submit,input2clicked]">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </center>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      eventTitle: "Perplexed",
      btn1click: false,
      btn2click: false,
      input1: "",
      input2: ""
    };
  },
  computed: {
    btn1clicked() {
      return this.btn1click ? this.$style.hideme : "";
    },
    input1clicked() {
      return this.btn1click ? "" : this.$style.hideme;
    },
    btn2clicked() {
      return this.btn2click ? this.$style.hideme : "";
    },
    input2clicked() {
      return this.btn2click ? "" : this.$style.hideme;
    }
  }
};
</script>
<style module lang = "stylus" >
@require '~@styles/theme';

$box-height = 250px;
$box-width = 350px;

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
  height: 60px;
}

.btn1, .btn2 {
  background-color: black;
  border: 1px solid $chartreuse;
  color: $chartreuse;
  font-family: 'Aldo the Apache';
  padding: 15px;
  font-size: 20px;
  border-radius: 5px;
  width: 140px;

  &:hover {
    box-shadow: inset 0px 0px 7px #86ff00;
  }
}

.orBox {
  height: 40px;
  font-family: QuickSand;
}

.field {
  clear: both;
  height: 30px;
  color: white;
  border: 0;
  outline: 0;
  width: ($box-width - 150px);
  font-size: 16px;
  background: #fff2;
  border-radius: 5px;
  padding-left: 5px;
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

.hideme {
  display: none;
}
</style>
