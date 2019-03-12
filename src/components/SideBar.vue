<template>
  <!-- Credits to: https://github.com/mbj36/vue-burger-menu -->
  <div>
    <div ref="sideNav" class="bm-menu" :style="getTransformXStyle(state.transform)">
      <nav class="bm-item-list">
        <slot></slot>
      </nav>
      <span class="bm-cross-button cross-style" @click="closeMenu" :class="{ hidden: !crossIcon }">
        <span
          v-for="(x, index) in 2"
          :key="x"
          class="bm-cross"
          :style="{ position: 'absolute', width: '3px', height: '14px',transform: index === 1 ? 'rotate(45deg)' : 'rotate(-45deg)'}"
        ></span>
      </span>
    </div>
    <div
      id="bm-backdrop"
      v-if="isSideBarOpen"
      :style="getOpacityStyle(state.backdropOpacity)"
      @click="closeMenu"
    ></div>
  </div>
</template>

<script>
import { interpolateEaseOutQuad } from "../js/utils.js";
import { setInterval } from "core-js";

export default {
  data() {
    return {
      isSideBarOpen: false
    };
  },
  computed: {
    state() {
      return {
        transform: 0,
        backdropOpacity: 0,
        isTouched: false
      };
    },
    animation() {
      return {
        fingerId: null,
        startX: null,
        startY: null,
        draggingStarted: false,
        previousX: null,
        previousY: null,
        wasInSidenavOnce: false,
        lastAnimationId: 0,
        lastSpeed: 0
      };
    }
  },
  props: {
    isOpen: {
      type: Boolean,
      required: false
    },
    right: {
      type: Boolean,
      required: false
    },
    width: {
      type: Number,
      required: false,
      default: 300
    },
    disableEsc: {
      type: Boolean,
      required: false
    },
    crossIcon: {
      type: Boolean,
      required: false,
      default: true
    },
    disableOutsideClick: {
      type: Boolean,
      required: false,
      default: false
    },
    extraClosePixels: {
      type: Number,
      default: 30
    },
    backdropOpacity: {
      type: Number,
      default: 0.5
    },
    animationDuration: {
      type: Number,
      default: 300
    },
    dragStartSensitivity: {
      type: Number,
      default: 40
    },
    swipeSensitivity: {
      type: Number,
      default: 10
    },
    defaultAnimationSensitivity: {
      type: Number,
      default: 40
    }
  },
  methods: {
    openMenu() {
      const {
        transform: startTransform,
        backdropOpacity: startOpacity
      } = this.state;

      const {
        animationDuration: fullAnimationDuration,
        width,
        backdropOpacity,
        extraClosePixels
      } = this.$props;

      let animationDuration =
        ((width - startTransform) * fullAnimationDuration) /
        (width + extraClosePixels);

      // if the speed caused a swipe, we adjust our animation speed to match swipe's momentum
      if (this.animation.lastSpeed > this.$props.swipeSensitivity) {
        animationDuration =
          (this.$props.defaultAnimationSensitivity * animationDuration) /
          this.animation.lastSpeed;
      }

      const transformAnimationFn = currentTime =>
        interpolateEaseOutQuad(
          currentTime,
          startTransform,
          width,
          animationDuration
        );

      const opacityAnimationFn = currentTime =>
        interpolateEaseOutQuad(
          currentTime,
          startOpacity,
          backdropOpacity,
          animationDuration
        );

      const onAnimationEnd = () => {
        this.setBusyState(false);
        this.isSideBarOpen = true;
        this.$emit("openSideBar");
      };

      this.animateSidebar(
        animationDuration,
        transformAnimationFn,
        opacityAnimationFn,
        onAnimationEnd
      );
    },
    closeMenu() {
      const {
        transform: startTransform,
        backdropOpacity: startOpacity
      } = this.state;

      const {
        animationDuration: fullAnimationDuration,
        extraClosePixels,
        width
      } = this.$props;

      let animationDuration =
        ((startTransform + extraClosePixels) * fullAnimationDuration) /
        (width + extraClosePixels);

      // if the speed caused a swipe, we adjust our animation speed to match swipe's momentum
      if (Math.abs(this.animation.lastSpeed) > this.$props.swipeSensitivity) {
        animationDuration =
          (this.$props.defaultAnimationSensitivity * animationDuration) /
          Math.abs(this.animation.lastSpeed);
      }

      const transformAnimationFn = currentTime =>
        interpolateEaseOutQuad(
          currentTime,
          startTransform,
          -1 * extraClosePixels,
          animationDuration
        );

      const opacityAnimationFn = currentTime =>
        interpolateEaseOutQuad(currentTime, startOpacity, 0, animationDuration);

      const onAnimationEnd = () => {
        this.setBusyState(false);
        this.$emit("closeSideBar");
        this.isSideBarOpen = false;
      };

      this.animateSidebar(
        animationDuration,
        transformAnimationFn,
        opacityAnimationFn,
        onAnimationEnd
      );
    },
    closeMenuOnEsc(e) {
      e = e || window.event;
      if (e.key === "Escape" || e.keyCode === 27) {
        this.closeMenu();
      }
    },
    touchstart(e) {
      const { transform } = this.state;
      if (this.animation.fingerId !== null) {
        // already touching it with another finger :D
        e.preventDefault();
        return;
      }

      if (e.touches.length !== 1) {
        // touching with multiple fingers
        return;
      }

      // if closed, check if the touch is from the left edge of the screen
      if (!open && e.touches[0].clientX > this.$props.dragStartSensitivity) {
        return;
      }

      this.animation.fingerId = e.touches[0].identifier;
      this.animation.startX = e.touches[0].clientX;
      this.animation.startY = e.touches[0].clientY;
      this.animation.startTransform = transform;
      this.animation.wasInSidenavOnce = false;
      this.animation.draggingStarted = false;
      this.animation.previousX = -999;
      this.animation.previousY = -999;

      // bind touchmove and end cancel events
      document.addEventListener("touchmove", this.touchmove, { passive: true });
      document.addEventListener("touchcancel", this.touchfinish, {
        passive: true
      });
      document.addEventListener("touchend", this.touchfinish, {
        passive: true
      });

      this.setTouchState(true);
    },
    touchmove(e) {
      const pivotTouch = [...e.changedTouches].find(
        t => this.animation.fingerId === t.identifier
      );
      // our finger that starting dragging on screen is not on the screen anymore
      if (!pivotTouch) {
        return;
      }

      if (
        Math.abs(pivotTouch.clientX - this.animation.previousX) < 1 &&
        Math.abs(pivotTouch.clientY - this.animation.previousY) < 1
      ) {
        // Do not over invoke move event
        return;
      }
      this.animation.lastSpeed = pivotTouch.clientX - this.animation.previousX;
      this.animation.previousX = pivotTouch.clientX;
      this.animation.previousY = pivotTouch.clientY;

      if (this.isSideBarOpen) {
        if (
          !this.animation.draggingStarted &&
          Math.abs(this.animation.startX - pivotTouch.clientX) <
            Math.abs(this.animation.startY - pivotTouch.clientY)
        ) {
          // we are scrolling on Y axis in the sidenav. we shall not move it.
          this.doTouchFinish(null);
          return;
        }
      }

      this.animation.draggingStarted = true;

      this.expandTo(
        this.animation.startTransform +
          (pivotTouch.clientX -
            Math.min(this.animation.startX, this.$props.width))
      );
    },
    touchfinish(e) {
      const pivotTouch = [...e.changedTouches].find(
        t => this.animation.fingerId === t.identifier
      );
      // our finger that starting dragging on screen is not on the screen anymore
      if (!pivotTouch) {
        return;
      }

      if (!this.animation.draggingStarted) {
        return this.doTouchFinish(null);
      }

      let shouldOpen = this.state.transform > this.$props.width / 2;
      if (this.animation.lastSpeed > this.$props.swipeSensitivity) {
        shouldOpen = true;
      } else if (this.animation.lastSpeed < -1 * this.$props.swipeSensitivity) {
        shouldOpen = false;
      }
      this.doTouchFinish(shouldOpen);
    },
    doTouchFinish(shouldOpen) {
      if (shouldOpen === true) {
        this.open();
      } else if (shouldOpen === false) {
        this.close();
      }
      document.removeEventListener("touchmove", this.touchmove);
      document.removeEventListener("touchcancel", this.touchfinish);
      document.removeEventListener("touchend", this.touchfinish);
      this.animation.fingerId = null;

      this.setTouchState(false);
    },
    setTouchState(isTouched) {
      this.$emit("onTouch", isTouched);
    },
    setBusyState(isBusy) {
      this.$emit("onBusy", isBusy);
    },
    expandTo(px) {
      px = Math.min(px, this.$props.width);
      const opacity = (this.$props.backdropOpacity * px) / this.$props.width;

      this.state.transform = px;
      this.state.backdropOpacity = opacity;
    },
    animateSidebar(
      animationDuration,
      transformAnimationFn,
      opacityAnimationFn,
      onAnimationEnd
    ) {
      const { lastAnimationId } = this.animation;
      let animationStartTime = null;
      let animationId = lastAnimationId + 1;
      this.animation.lastAnimationId = animationId;
      this.setBusyState(true);

      const animate = time => {
        if (animationId !== this.animation.lastAnimationId) {
          console.log(1);
          // looks like a new animation triggered while this was in progress... ignore this one.
          return;
        }
        if (animationDuration === 0) {
          console.log(2);
          // nothing to animate, just finish it already
          onAnimationEnd();
          return;
        }

        let timePassed = 0;
        if (animationStartTime === null) {
          animationStartTime = time;
        } else {
          timePassed = Math.min(time - animationStartTime, animationDuration);
        }
        console.log("anim:" + timePassed);

        this.$nextTick(() => {
          const targetOpacity = opacityAnimationFn(timePassed);
          const targetTransform = transformAnimationFn(timePassed);

          this.state.transform = targetTransform;
          this.state.backdropOpacity = targetOpacity;
        });

        if (timePassed < animationDuration) {
          window.requestAnimationFrame(animate);
        } else {
          console.log(3);
          onAnimationEnd();
        }
      };
      window.requestAnimationFrame(animate);
    },
    documentClick(e) {
      let target = null;
      if (e && e.target) {
        target = e.target;
      }
      if (
        target.className !== "bm-menu" &&
        target.className !== "bm-toggle" &&
        this.isSideBarOpen &&
        !this.disableOutsideClick
      ) {
        this.closeMenu();
      }
    },
    getOpacityStyle(opacity) {
      return { opacity };
    },
    getTransformXStyle(px) {
      const { width } = this.$props;
      return {
        transform: `translate3d(${px - width}px, 0, 0)`
      };
    }
  },
  mounted() {
    if (!this.disableEsc) {
      document.addEventListener("keyup", this.closeMenuOnEsc);
    }
    if (this.right) {
      this.$refs.sideNav.style.left = "auto";
      this.$refs.sideNav.style.right = "0px";
    }
  },
  created() {
    this.state.transform = -1 * this.$props.extraClosePixels;
    // document.addEventListener("touchstart", this.touchstart, {
    //   passive: false
    // });
    // document.addEventListener("click", this.documentClick);
  },
  destroyed() {
    document.removeEventListener("keyup", this.closeMenuOnEsc);
    // document.removeEventListener("click", this.documentClick);
    document.removeEventListener("touchstart", this.touchstart);
  },
  watch: {
    isOpen: {
      deep: true,
      immediate: true,
      handler(newValue, oldValue) {
        this.$nextTick(() => {
          if (newValue !== oldValue) {
            if (newValue) this.openMenu();
            else this.closeMenu();
          }
        });
      }
    },
    right: {
      deep: true,
      immediate: true,
      handler(oldValue, newValue) {
        if (oldValue) {
          this.$nextTick(() => {
            this.$refs.sideNav.style.left = "auto";
            this.$refs.sideNav.style.right = "0px";
            document.querySelector(".cross-style").style.right = "250px";
          });
        }
      }
    }
  }
};
</script>

<style lang="stylus">
@import '../styles/colors.styl';

:global {
  .cross-style {
    position: absolute;
    top: 12px;
    right: 2px;
    cursor: pointer;
  }

  .bm-cross {
    background: #bdc3c7;
  }

  .bm-cross-button {
    height: 24px;
    width: 24px;
  }

  .bm-cross-button.hidden {
    display: none;
  }

  .bm-menu {
    height: 100%; /* 100% Full-height */
    width: 300px;
    position: fixed; /* Stay in place */
    z-index: 1000; /* Stay on top */
    top: 0;
    left: 0;
    background-color: rgb(63, 63, 65); /* Black */
    overflow-x: hidden; /* Disable horizontal scroll */
    padding-top: 60px; /* Place content 60px from the top */
    overflow-y: auto;
    will-change: transform;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.6);
  }

  .bm-overlay {
    background: rgba(0, 0, 0, 0.3);
  }

  .bm-item-list {
    color: #b8b7ad;
    margin-left: 10%;
    font-size: 20px;
  }

  .bm-item-list > * {
    display: flex;
    text-decoration: none;
    padding: 0.7em;
  }

  .bm-item-list > * > span {
    margin-left: 10px;
    font-weight: 700;
    color: white;
  }

  #bm-backdrop {
    opacity: 0.5;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    will-change: opacity;
    background: $black;
    z-index: 900;
    touch-action: none;
  }
}
</style>