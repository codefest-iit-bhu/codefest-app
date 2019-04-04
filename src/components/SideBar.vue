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
          :style="{ position: 'absolute', width: '3px', height: '24px',transform: index === 1 ? 'rotate(45deg)' : 'rotate(-45deg)'}"
        ></span>
      </span>
    </div>
    <div
      id="bm-backdrop"
      v-if="showBackdrop"
      :style="getOpacityStyle(state.backdropOpacity)"
      @click="closeMenu"
    ></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isSideBarOpen: false,
      backdropOpacity: 0,
      transform: 0,
      showBackdrop: false
    };
  },
  computed: {
    state() {
      return {
        transform: this.transform,
        backdropOpacity: this.backdropOpacity,
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
    propBackdropOpacity: {
      type: Number,
      default: 0.5
    },
    animationDuration: {
      type: Number,
      default: 0.3
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
      const { transform: startTransform } = this.$data;

      const {
        animationDuration: fullAnimationDuration,
        width,
        propBackdropOpacity: backdropOpacity,
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

      const transformAnim = {
        transform: width
      };

      const opacityAnim = {
        backdropOpacity
      };

      const animHandlers = {
        onComplete: () => {
          this.isSideBarOpen = true;
          this.$emit("openSideBar");
        },
        onStart: () => (this.showBackdrop = true)
      };

      this.animateSidebar(
        animationDuration,
        transformAnim,
        opacityAnim,
        animHandlers
      );
    },
    closeMenu() {
      const { transform: startTransform } = this.state;

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

      const transformAnim = {
        transform: -1 * extraClosePixels
      };

      const opacityAnim = {
        backdropOpacity: 0
      };

      const animHandlers = {
        onComplete: () => {
          this.isSideBarOpen = false;
          this.showBackdrop = false;
          this.$emit("closeSideBar");
        }
      };

      this.animateSidebar(
        animationDuration,
        transformAnim,
        opacityAnim,
        animHandlers
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
    expandTo(px) {
      px = Math.min(px, this.$props.width);
      const opacity =
        (this.$props.propBackdropOpacity * px) / this.$props.width;

      this.transform = px;
      this.backdropOpacity = opacity;
    },
    animateSidebar(
      animationDuration,
      transformAnimationData,
      opacityAnimationData,
      animationHandlers
    ) {
      TweenMax.to(this.$data, animationDuration, {
        ...transformAnimationData,
        ...opacityAnimationData,
        ...animationHandlers,
        ease: Power4.easeOut
      });
    },
    getOpacityStyle(opacity) {
      return { opacity };
    },
    getTransformXStyle(px) {
      const { width } = this.$props;
      return {
        width: `${width}px`,
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
    this.transform = -1 * this.extraClosePixels;
    // document.addEventListener("touchstart", this.touchstart, {
    //   passive: false
    // });
  },
  destroyed() {
    document.removeEventListener("keyup", this.closeMenuOnEsc);
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
@require '~@styles/theme';

:global {
  .cross-style {
    position: absolute;
    top: 12px;
    left: 12px;
    cursor: pointer;
    padding-left: 7px;
  }

  .bm-cross {
    background: #bdc3c7;
  }

  .bm-cross-button {
    height: 30px;
    width: 30px;
  }

  .bm-cross-button.hidden {
    display: none;
  }

  .bm-menu {
    padding-left: 10%;
    height: 100%; /* 100% Full-height */
    position: fixed; /* Stay in place */
    z-index: 1000; /* Stay on top */
    top: 0;
    left: 0;
    background-color: rgba(63, 63, 65, 0.5); /* Black */
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
    font-size: 20px;
  }

  .bm-item-list > * {
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