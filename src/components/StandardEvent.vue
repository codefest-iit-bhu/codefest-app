<template>
  <div :class="[$style.event, $style[$mq], eventActiveClass]">
    <div :class="eventCellClass" >
      <div :class="$style.eventCardLeft">
        <div :class="$style.eventCardLeft" v-if="event.id%2==0" @mouseenter="toggleOpen" @mouseleave="toggleOpen" @click="navigateToDetails">
          <div :class="$style.iconLeft" >
            <div :class="$style.iconInnerLeft">
              <img :src="event.icon" :class="$style.imgLeft" />
            </div>
          </div>

          <svg :class="$style.cnctr">
            <line x1="220" y1="15" x2="260" y2="15" style="stroke:rgb(7,249,254);stroke-width:1" />
            <line x1="240" y1="10" x2="265" y2="10" style="stroke:rgb(7,249,254);stroke-width:1" />
            <line x1="265" y1="10" x2="285" y2="25" style="stroke:rgb(7,249,254);stroke-width:1" />
          </svg>
          
          <Button  :text= "event.title"
            class="btnn"
            :class="$style.btn"
          />
          <Card :title="event.title" :text="event.summary" :class="$style.crd" 
            class="card"
          />


        </div>
        <div :class="$style.eventCardRight" @mouseenter="toggleOpen" @mouseleave="toggleOpen" @click="navigateToDetails" v-else >
          <CardRev :title="event.title" :text="event.summary" :class="$style.crdRev" 
            class="card"
          />
          <ButtonRev  :text= "event.title" :class="$style.btnRev" 
            class="btnn"
          />
          <svg :class="$style.cnctrRev" >
            <line x1="230" y1="15" x2="270" y2="15" style="stroke:rgb(7,249,254);stroke-width:1" />
            <line x1="225" y1="10" x2="250" y2="10" style="stroke:rgb(7,249,254);stroke-width:1" />
            <line x1="225" y1="10" x2="205" y2="25" style="stroke:rgb(7,249,254);stroke-width:1" />
          </svg>
          <div :class="$style.iconRight" >
            <div :class="$style.iconInnerRight">
              <img :src="event.icon" :class="$style.imgRight" />
            </div>
          </div>
        </div>
      </div>
      <!-- <div>
        <EventCard :title="event.title" :summary="event.summary" />
      </div> -->
      
      <!-- <div
        :class="$style.cell"
        :style="eventWidthStyle" 
        @mouseenter="toggleOpen"
        @mouseleave="toggleOpen"
      > -->
        <!-- <canvas
          :class="$style.normalCanvas"
          ref="initialCanvas"
          :style="canvasOpacityStyle(true)"
          v-if="!isMinimal"
        />
        <canvas
          :class="$style.glitchedCanvas"
          ref="finalCanvas"
          :style="canvasOpacityStyle(false)"
        /> -->
        <!-- <div :class="$style.txt"> -->
          <!-- <p :class="$style.summary" style="display:block;">{{event.title}}</p> -->
          <!-- <span :class="$style.summary">{{event.title}}</span> -->
          <!-- <p :class="$style.summary">
            <span>{{event.title}}<br></span>
            <span ref="eventSummary"></span>
            <span :class="$style.blink">|</span>
          </p> -->
        <!-- </div> -->
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
import { TypingAnim, getRandom, isMinimal } from "@js/utils";
import Button from "./layouts/Button.vue"
import ButtonRev from "./layouts/ButtonRev.vue"
import EventCard from './layouts/EventCard.vue'
import Card from './layouts/Card.vue'
import CardRev from './layouts/CardRev.vue'
export default {
  components: {
    Button,
    ButtonRev,
    EventCard,
    Card,
    CardRev
  },
  data() {
    return {
      shouldOpen: false,
      shouldOpenRight: false,
      shouldOpenLeft: false,
      e_id:-1,
      openProgress: 0,
      maxWidth: 0,
      minSize: 0,
    };
  },
  props: {
    event: {
      required: true,
      type: Object,
    },
    id: {
      required: true,
      type: Number,
    },
    keepOpen: {
      required: false,
      type: Boolean,
      default: false,
    },
  },
  methods: {
    animateGlitchOpacity(canvas, duration, isAppearIn) {
      if (!canvas) return;
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
        }
      };
      return step();
    },
    glitch(isAppearIn) {
      if (!this.image) {
        return;
      }
      const { initialCanvas, finalCanvas } = this.$refs;
      this.animateGlitchOpacity(initialCanvas, 800, !isAppearIn);
      this.animateGlitchOpacity(finalCanvas, 800, isAppearIn);
    },
    canvasOpacityStyle(isNormalCanvas) {
      return {
        opacity: isNormalCanvas ? 1 - this.openProgress : this.openProgress,
      };
    },
    toggleEvent(shouldOpen) {
      TweenLite.to(this.$data, 0.8, { openProgress: shouldOpen ? 1 : 0 });
      this.glitch(shouldOpen);

      if (shouldOpen) this.animTyping.type();
      else this.animTyping.erase();
    },
    toggleopac(){
      const id=this.e_id
      const a=document.getElementsByClassName("btnn")[id-1];
      const c=document.getElementsByClassName("card")[id-1];
      if (this.shouldOpen) {
        a.setAttribute("style", "display:none !important");
        c.setAttribute("style", "display:flex !important");
      }
      else{
        a.setAttribute("style", "display:flex !important");
        c.setAttribute("style", "display:none !important");
      }
    },
    toggleOpen() {
      const dir=this.event.id
      this.shouldOpen= !this.shouldOpen
      this.e_id=dir;
    },
    resetState() {
      this.maxWidth = (this.isMinimal ? 1.0 : 0.7) * window.innerWidth;
      this.minSize = this.isMinimal ? 0.75 * 150 : 150;
    },
    navigateToDetails() {
      this.$router.push(`/events/${this.event.name}`);
    },
  },
  mounted() {
    function drawInCanvas(canvas, image) {
      if (!canvas) return;
      var context = canvas.getContext("2d");
      canvas.setAttribute("width", image.width);
      canvas.setAttribute("height", image.height);
      context.drawImage(image, 0, 0);
    }

    this.animTyping = new TypingAnim(
      this.$refs.eventSummary,
      this.event.summary,
      // this.$refs.eventTitle,
      // this.event.title,
    );

    var img = new Image();
    img.src = this.event.icon;
    img.onload = () => {
      this.image = img;
      const { initialCanvas, finalCanvas } = this.$refs;
      drawInCanvas(initialCanvas, img);
      drawInCanvas(finalCanvas, img);
      if (this.keepOpen) {
        this.$nextTick(() => (this.shouldOpen = true));
      }
    };
  },
  beforeMount() {
    this.resetState();
  },
  computed: {
    eventCellClass() {
      return this.id % 2 == 0 ? this.$style.even : this.$style.odd;
    },
    eventActiveClass() {
      return this.isOpen || this.shouldOpen ? this.$style.visible : "";
    },
    eventWidthStyle() {
      const width = Math.max(this.minSize, this.openProgress * this.maxWidth);
      return {
        width: `${width}px`,
      };
    },
    eventTitleStyle() {
      const marginLeft = this.isMinimal ? undefined : "15px";
      const marginTop = this.isMinimal ? "15px" : undefined;
      return { marginLeft, marginTop };
    },
    isOpen() {
      return this.openProgress === 1;
    },
    isMinimal() {
      return isMinimal(this.$mq);
    },
  },
  watch: {
    shouldOpen: function(shouldOpen, oldVal) {
      if (oldVal == shouldOpen) return;
      this.toggleopac();
    },
    $mq: function() {
      this.resetState();
    },
  },
  
};
</script>

<style lang="stylus" module>
@require '~@styles/anims';

$cell-collapsed-size = 150px;
$cell-expanded-size = 200px;



.crd{
  display: none !important;
  margin-left: 340px;
}
.crdRev{
  display: none !important;
  margin-right: 340px;
}

.btn{
  display: flex;
  margin-left: 30px;
}

.btnRev{
  display: flex;
  margin-right: 30px;
}

.cnctrRev {
  position: absolute;
  right: 60px;
  top: 25px;
}

.cnctr{
  position: absolute;
  left: -130px;
  top: 25px;
}
.eventCardLeft{
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.eventCardRight{
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.iconLeft{
  height: 88px;
  width: 88px;
  border: 2px solid $waterloo;
  border-radius: 50%;
  //padding: 30px;
  margin-right: 120px; 
  margin-bottom:70px;
}

.iconInnerLeft{
  height: 70px;
  width:  70px;
  border: 2px solid rgba(7,249,254,.5);
  border-radius: 50%;
  //padding: 30px;
  //margin-right: 120px;
  margin:7px; 
  transform: rotateY(0deg) rotate(-45deg);
  border-left-color:transparent;

}

.iconRight{
  height: 88px;
  width: 88px;
  border: 2px solid $waterloo;
  border-radius: 50%;
  //padding: 30px;
  margin-left: 120px;
  margin-bottom: 70px;
}


.iconInnerRight{
  height: 70px;
  width:  70px;
  border: 2px solid rgba(7,249,254,.5);
  border-radius: 50%;
  margin: 7px;
  transform: rotateY(0deg) rotate(45deg);
  border-right-color:transparent;
  // margin-left: 120px;
}

.imgLeft{
  height: 50%;
  margin: 15px;
  transform: rotateY(0deg) rotate(45deg);
}
.imgRight{
  height: 50%;
  margin:15px;
  transform: rotateY(0deg) rotate(-45deg);

}

.event {
  --event-collapsed-size: $cell-collapsed-size;
  --event-size: $cell-expanded-size;
  height: var(--event-size);
  position: relative;
  margin: 0 20px 25px;
  cursor: pointer;
}

.whiteTitle {
  display: flex;
  color: var(--text-color);
  font-family: 'Baloo Bhaina 2';

  h3 {
    $font-size: 32px;
  }
}

.cell {
  // box-shadow: var(--icon-shadow);
  width: 800px;
  height: 100%;
  // background: $waterloo;
  // border-radius: calc((var(--event-size) / 2));
  background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
}

.odd {
  // height: 100%;
  // display: flex;
  // justify-content: flex-start;
  // align-items: center;

  .normalCanvas {
    float: left;
  }

  .glitchedCanvas {
    float: right;
  }

  .txt {
    text-align: left;
    left: 10px;
  }

  .whiteTitle {
    order: 2;
    margin-left: 15px;
  }
}

.even {
  // height: 100%;
  // display: flex;
  // justify-content: flex-end;
  // align-items: center;

  .normalCanvas {
    float: right;
  }

  .glitchedCanvas {
    float: left;
  }

  .txt {
    text-align: right;
    left: -15px;
  }

  .whiteTitle {
    order: 0;
    margin-right: 15px;
  }
}

.txt {
  color: $black;
  $font-size: 16px;
  pointer-events: none;
  align-items: center;
  height: 100%;
  display: flex;
  transition: opacity 400ms;
  opacity: 0;
  overflow: visible;
  position: relative;

  .summary {
    font-family: 'Quicksand';
    padding: 2px 10px;
    text-align: justify;
    $font-size: 24px;
    font-weight: 600;
    vertical-align: middle;
    color: $mystic;
  }
}

.normalCanvas{
  width: calc((var(--event-collapsed-size) / 1));
  height: calc((var(--event-collapsed-size) / 1));
  padding: 30px;
  border-radius: calc((var(--event-size) / 2));
} 
.glitchedCanvas {
  width: calc((var(--event-size) / 1));
  height: calc((var(--event-size) / 1));
  padding: 30px;
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
    margin: 0 20px 60px;

    .whiteTitle {
      margin: 15px 0 0 0;

      h3 {
        $font-size: 24px;
      }
    }

    .txt {
      $font-size: 12px;
    }

    .odd {
      justify-content: flex-end;

      .whiteTitle {
        order: -1;
      }
    }

    .even, .odd {
      flex-flow: column;
    }
  }

  &.visible {
    .txt {
      opacity: 1;
    }

    .cell {
      // clip-path: polygon(20% 0,100% 0,100% 70%,80% 100%,0 100%,0 30% );
      clip-path: polygon(0 0,90% 0,100% 30%,100% 100%,10% 100%,0 70% );
      width: 70%;
    }

    &.md .cell, &.lg .cell, &.xl .cell {
      animation: timeline-border-green 1s ease-in-out infinite alternate;
    }
  }
}



</style>
