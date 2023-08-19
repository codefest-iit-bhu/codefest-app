<template>
  <div :class="checkpointClass">
    <div :class="$style.dateTime">
      <span v-if="data.isMajor">
        <i class="fa fa-calendar-alt" aria-hidden="true"></i>
        {{ computedDate }}
      </span>
      <span v-else>
        <i class="fa fa-clock" aria-hidden="true"></i>
        {{ computedTime }}
      </span>
    </div>
    <div :class="$style.event" :title="data.summary">
      <span>
        <h4>{{ data.title }}</h4>
      </span>
    </div>
  </div>
</template>

<script>
import { formatDateTo12HoursTime } from "@js/utils";

export default {
  props: {
    data: {
      required: true,
      type: Object,
    },
  },
  computed: {
    checkpointClass() {
      return {
        [this.$style.checkpointWrapper]: true,
        [this.$style.done]: this.isDone,
        [this.$style.major]: this.data.isMajor,
      };
    },
    isDone() {
      const { start, end } = this.data;
      const today = new Date();
      return !!end ? end <= today : start <= today;
    },
    computedDate() {
      const { start: date } = this.data;
      const day = date.getDate();
      const month = date.toLocaleString("en-us", { month: "long" });
      return `${day} ${month}`;
    },
    computedTime() {
      const { start, end } = this.data;

      if (end) {
        return `${formatDateTo12HoursTime(start)} - ${formatDateTo12HoursTime(
          end
        )}`;
      } else return formatDateTo12HoursTime(start);
    },
  },
};
</script>

<style module lang="stylus">
@require '~@styles/anims';

$circle-small-size = 15px;
$circle-large-size = 20px;
$line-empty-background = $white;
$line-filled-background = $waterloo;
$circle-border-color = $waterloo;
$circle-empty-background = $white;
$circle-filled-background = $waterloo;
$circle-transparent-background = transparent;

.checkpointWrapper {
  margin: 0 auto;
  padding: 0;
  position: relative;
  height: 100px;

  &:before {
    content: '';
    position: absolute;
    width: $circle-small-size;
    height: $circle-small-size;
    left: -5px;
    top: 5px;
    background-color: $circle-empty-background;
    border: 1px solid $circle-border-color;
    border-radius: 50%;
    z-index: 1;

    ~/.done^[1..-1] {
      background-color: $circle-filled-background;
    }

    ~/.notdone^[1..-1] {
      background-color: $circle-transparent-background;
      border: 3px solid $waterloo70;
    }

    ~/.major^[1..-1] {
      left: -8px;
      width: $circle-large-size;
      height: $circle-large-size;
      animation: timeline-border-green 1.5s ease-in-out infinite alternate;
    }
  }

  &:after {
    content: '';
    position: absolute;
    margin: auto;
    z-index: -2;
    border-right: 5px solid $line-empty-background;
    top: 0;
    bottom: 0;

    ~/.done^[1..-1] {
      border-color: $line-filled-background;
    }

    ~/.major^[1..-1] {
    }
  }

  &:first-child {
    &:before {
      top: 0;
    }
  }

  &:last-child {
    &:before {
      top: 0;
    }

    &:after {
      display: none;
    }
  }

  .dateTime, .event {
    position: relative;
    background: transparent;
    margin: 0;
    color: var(--text-color);
    border-radius: 4px;
  }

  .dateTime {
    width: 200px;
    height: 36px;
    padding: 2px 5px;
    margin-left: 25px;
    $font-size: 14px;
    line-height: 30px;
    text-align: center;
    border: 2px solid $waterloo;
    border-radius: 18px;
    font-family: 'Quicksand';
    font-weight: 600;

    i {
      padding-right: 5px;
    }

    ~/.major ^[1..-1] {
      width: 150px;
      border-radius: 4px;
    }
  }

  .event {
    padding: 5px;
    padding-left: 25px;

    span h4 {
      margin: 0;
      font-family: 'Roboto Slab';
      $font-size: 18px;
    }
  }
}
</style>
