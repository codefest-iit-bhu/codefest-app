<template>
  <div :class="[$style.countdown, $style[$mq]]">
    <div :class="$style.block">
      <div :class="$style.value">{{ days | double_digit }}</div>
      <!-- <div :class="$style.txt">Days</div> -->
    </div>

    <div :class="$style.block">
      <div :class="$style.value">{{ hours | double_digit }}</div>
      <!-- <div :class="$style.txt">Hours</div> -->
    </div>

    <div :class="$style.block">
      <div :class="$style.value">{{ minutes | double_digit }}</div>
      <!-- <div :class="$style.txt">Minutes</div> -->
    </div>

    <div :class="$style.block">
      <div :class="$style.value">{{ seconds | double_digit }}</div>
      <!-- <div :class="$style.txt">Seconds</div> -->
    </div>
  </div>
</template>

<script>
export default {
  props: {
    until: {
      type: Date,
      required: true
    }
  },
  data() {
    return {
      now: Math.trunc(new Date().getTime() / 1000)
    };
  },
  computed: {
    untilInMillisecond() {
      return Math.trunc(this.until.getTime() / 1000);
    },
    timeDiff() {
      return this.untilInMillisecond - this.now;
    },
    days() {
      return Math.trunc(this.timeDiff / 60 / 60 / 24);
    },
    hours() {
      return Math.trunc(this.timeDiff / 60 / 60) % 24;
    },
    minutes() {
      return Math.trunc(this.timeDiff / 60) % 60;
    },
    seconds() {
      return this.timeDiff % 60;
    }
  },
  mounted() {
    window.setInterval(() => {
      this.now = Math.trunc(new Date().getTime() / 1000);
    }, 1000);
  },
  filters: {
    double_digit(value) {
      if (value < 0) {
        return "00";
      }
      if (value.toString().length <= 1) {
        return `0${value}`;
      }
      return value;
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.countdown {
  font-family: 'Roboto Slab';
  display: flex;
  flex-flow: row;

  .block {
    display: flex;
    flex-flow: column;
    border: 3px solid $outer-space;
    padding: 10px 20px;

    .txt {
      text-align: center;
      font-size: 21px;
    }

    .value {
      text-align: center;
      font-size: 50px;
      font-weight: 600;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 24px;
      }
    }
  }
}
</style>

