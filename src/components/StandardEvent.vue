<template>
  <div :class="[$style.event, $style[$mq], eventActiveClass]">
    <div :class="eventCellClass">
      <div :class="$style.whiteTitle">
        <h3>{{ event.title }}</h3>
      </div>
      <div :class="$style.cell" @mouseenter="shouldOpen = true" @mouseleave="shouldOpen = false">
        <canvas :class="$style.normalCanvas" ref="initialCanvas"/>
        <canvas :class="$style.glitchedCanvas" ref="finalCanvas"/>
        <div :class="$style.txt">
          <p :class="$style.summary">
            <span ref="eventSummary"></span>
            <span :class="$style.blink">|</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// TODO: Use GSAP to animate everything, instead of CSS + JS hybrid.
import { TypingAnim, getRandom } from "@js/utils";

export default {
  data() {
    return {
      shouldOpen: false,
      isOpen: false
    };
  },
  props: {
    event: {
      required: true,
      type: Object
    },
    id: {
      required: true,
      type: Number
    },
    keepOpen: {
      required: false,
      type: Boolean,
      default: false
    }
  },
  methods: {
    animateGlitchOpacity(canvas, duration, isAppearIn) {
      var that = this;
      var image = this.image;
      var verticalSlices = Math.round(image.height / 20);
      var maxHorizOffset = 30;

      var start = new Date().getTime();
      var context = canvas.getContext("2d");

      var step = function() {
        var timestamp = new Date().getTime();
        var progress = Math.min((timestamp - start) / duration, 1);
        canvas.style.opacity = isAppearIn ? progress : 1 - progress;

        context.clearRect(0, 0, canvas.width, canvas.height);

        for (var i = 0; i < verticalSlices; i++) {
          var horizOffset = getRandom(
            -Math.abs(maxHorizOffset),
            Math.abs(maxHorizOffset)
          );
          context.drawImage(
            image,
            0,
            i * verticalSlices,
            image.width,
            i * verticalSlices + verticalSlices,
            horizOffset,
            i * verticalSlices,
            image.width,
            i * verticalSlices + verticalSlices
          );
        }

        if (progress < 1) requestAnimationFrame(step);
        else {
          context.clearRect(0, 0, canvas.width, canvas.height);
          context.drawImage(image, 0, 0);
          that.isOpen = isAppearIn;
        }
      };
      return step();
    },
    glitch(isAppearIn, event) {
      if (!this.image) {
        return;
      }
      this.animateGlitchOpacity(this.$refs.initialCanvas, 800, !isAppearIn);
      this.animateGlitchOpacity(this.$refs.finalCanvas, 800, isAppearIn);

      if (isAppearIn) this.animTyping.type();
      else this.animTyping.erase();
    }
  },
  mounted() {
    function drawInCanvas(canvas, image) {
      var context = canvas.getContext("2d");
      canvas.setAttribute("width", image.width);
      canvas.setAttribute("height", image.height);
      context.drawImage(image, 0, 0);
    }

    this.animTyping = new TypingAnim(
      this.$refs.eventSummary,
      this.event.summary
    );

    var img = new Image();
    img.src = this.event.image;
    img.onload = () => {
      this.image = img;
      drawInCanvas(this.$refs.initialCanvas, img);
      drawInCanvas(this.$refs.finalCanvas, img);
      if (this.keepOpen) {
        this.$nextTick(() => (this.shouldOpen = true));
      }
    };
  },
  computed: {
    eventCellClass() {
      return this.id % 2 == 0 ? this.$style.even : this.$style.odd;
    },
    eventActiveClass() {
      return this.isOpen || this.shouldOpen ? this.$style.visible : "";
    }
  },
  watch: {
    shouldOpen: function(shouldOpen, oldVal) {
      if (oldVal == shouldOpen) return;
      this.glitch(shouldOpen);
    }
  }
};
</script>

<style lang="stylus" module>
@require '~@styles/theme';
@require '~@styles/anims';
@require '~@styles/mixins';

$cell-collapsed-size = 150px;

.event {
  --event-size: $cell-collapsed-size;
  clear: both;
  z-index: 0;
  height: var(--event-size);
  position: relative;
  margin: 0 20px 50px;
}

.whiteTitle {
  color: $white;
  font-family: 'Aldo the Apache';

  h3 {
    font-size: 32px;
  }
}

.cell {
  clear: both;
  box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3);
  width: var(--event-size);
  height: 100%;
  background: $chartreuse;
  cursor: pointer;
  border-radius: calc((var(--event-size) / 2));
  transition: width 2.5s ease-out;

  &:hover {
    transition-duration: 0.5s;
  }
}

.odd {
  height: 100%;
  display: flex;
  flex-flow: row;
  justify-content: flex-start;
  align-items: center;

  .normalCanvas {
    float: left;
  }

  .glitchedCanvas {
    float: right;
  }

  .txt {
    text-align: left;
  }

  .whiteTitle {
    order: 2;
    margin-left: 15px;
  }
}

.even {
  height: 100%;
  display: flex;
  flex-flow: row;
  justify-content: flex-end;
  align-items: center;

  .normalCanvas {
    float: right;
  }

  .glitchedCanvas {
    float: left;
  }

  .txt {
    text-align: right;
  }

  .whiteTitle {
    order: 0;
    margin-right: 15px;
  }
}

.txt {
  color: $black;
  font-size: 16px;
  pointer-events: none;
  align-items: center;
  height: 100%;
  display: flex;
  transition: opacity 400ms;
  opacity: 0;

  .summary {
    font-family: 'Courier New';
    padding: 2px 10px;
    text-align: justify;
    font-weight: 600;
    vertical-align: middle;
  }
}

.normalCanvas, .glitchedCanvas {
  width: var(--event-size);
  height: var(--event-size);
  padding: 35px;
}

.glitchedCanvas {
  opacity: 0;
  pointer-events: none;
}

.blink {
  animation: blink 500ms infinite alternate;
}

.event {
  &.xs, &.sm {
    --event-size: 0.75 * $cell-collapsed-size;

    .whiteTitle h3 {
      font-size: 24px;
    }

    .txt {
      font-size: 12px;
    }
  }

  &.visible {
    .txt {
      opacity: 1;
    }

    .cell {
      width: 70%;
    }
  }
}
</style>
