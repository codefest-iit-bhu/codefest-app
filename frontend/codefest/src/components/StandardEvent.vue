<template>
  <div :class="$style.event">
    <div
      :class="[$style.cell, eventCellClass]"
      @mouseenter="glitch(true, $event)"
      @mouseleave="glitch(false, $event)"
    >
      <canvas :class="$style.normalCanvas" ref="initialCanvas"/>
      <canvas :class="$style.glitchedCanvas" ref="finalCanvas"/>
      <div :class="$style.txt">
        <h3>{{ event.title }}</h3>
        <br>
        <p :class="$style.summary">
          <span ref="eventSummary"></span>
          <span :class="$style.blink">|</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { TypingAnim, getRandom } from "../js/utils";

export default {
  props: ["event", "id"],
  methods: {
    animateGlitchOpacity(canvas, duration, isAppearIn) {
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
        }
      };
      return step();
    },
    glitch(isAppearIn, event) {
      this.animateGlitchOpacity(this.$refs.initialCanvas, 1500, !isAppearIn);
      this.animateGlitchOpacity(this.$refs.finalCanvas, 1500, isAppearIn);

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

    var img = new Image();
    img.src = this.event.image;
    img.onload = () => {
      this.image = img;
      drawInCanvas(this.$refs.initialCanvas, img);
      drawInCanvas(this.$refs.finalCanvas, img);
    };

    this.animTyping = new TypingAnim(
      this.$refs.eventSummary,
      this.event.summary
    );
  },
  computed: {
    eventCellClass() {
      return this.id % 2 == 0 ? this.$style.even : this.$style.odd;
    }
  }
};
</script>

<style lang="stylus" module>
@import '../styles/theme.styl';
@import '../styles/anims.styl';
@import '../styles/colors.styl';

$cell-collapsed-size = 150px;

.event {
  clear: both;
  z-index: 0;
  height: $cell-collapsed-size;
}

.cell {
  clear: both;
  box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3);
  width: $cell-collapsed-size;
  height: 100%;
  margin-bottom: 50px;
  background: $chartreuse;
  cursor: pointer;
  border-radius: ($cell-collapsed-size / 2);
  transition: width 3s ease-out;

  &:hover {
    width: 70%;
    transition-duration: 0.5s;

    .txt {
      display: block;
    }

    .txt h3 {
      opacity: 1;
    }
  }

  &.odd {
    float: left;

    .normalCanvas {
      float: left;
    }

    .glitchedCanvas {
      float: right;
    }

    .txt {
      text-align: left;
    }
  }

  &.even {
    float: right;

    .normalCanvas {
      float: right;
    }

    .glitchedCanvas {
      float: left;
    }

    .txt {
      text-align: right;
    }
  }
}

.txt {
  color: $black;
  font-size: 16px;
  pointer-events: none;
}

.txt h3 {
  font-family: 'Aldo the Apache';
  margin-top: 20px;
  font-size: 50px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 1s ease-out;
}

.summary {
  font-family: 'Courier New';
  padding: 2px 10px;
  text-align: justify;
  font-weight: 600;
}

.normalCanvas, .glitchedCanvas {
  width: $cell-collapsed-size;
  height: $cell-collapsed-size;
  padding: 35px;
}

.glitchedCanvas {
  opacity: 0;
  pointer-events: none;
}

.blink {
  animation: blink 500ms infinite alternate;
}
</style>
