<template>
  <header ref="header" :class="$style.hero">
    <div ref="title" :class="$style.title">
      <h1>Codefest'19</h1>
    </div>
    <canvas ref="rains" :class="$style.rains"></canvas>
  </header>
</template>

<script>
import Nav from "@components/Nav";

export default {
  components: {
    Nav
  },
  mounted() {
    const c = this.$refs.rains;
    var ctx = c.getContext("2d");
    c.height = window.innerHeight;
    c.width = window.innerWidth;
    var code = "{}-+=xyz*&%print$;':<>?/";
    code = code.split("");
    var font_size = 40;
    var columns = (2 * c.width) / font_size;
    var drops = [];
    for (var x = 0; x < columns; x++) drops[x] = 1;
    function draw() {
      ctx.fillStyle = "rgba(0, 0, 0, 0.03)";
      ctx.fillRect(0, 0, c.width, c.height);
      ctx.fillStyle = "#86ff00";
      ctx.font = font_size + "px Courier New";
      for (var i = 0; i < drops.length; i++) {
        var text = code[Math.floor(Math.random() * code.length)];
        ctx.fillText(text, i * font_size, drops[i] * font_size);

        if (drops[i] * font_size > c.height && Math.random() > 0.975)
          drops[i] = 0;

        drops[i]++;
      }
    }
    setInterval(draw, 33);

    window.onscroll = function() {
      stickOnScroll();
    };

    var title = this.$refs.title;
    var offset = title.offsetTop;

    let center = { top: title.style.top, left: title.style.left };

    function stickOnScroll() {
      if (window.pageYOffset > offset) {
        title.style.position = "fixed";
        title.style.top = 0;
        title.style.left = 0;
      } else {
        title.style.position = "absolute";
        title.style.left = center["left"];
        title.style.top = center["top"];
      }
    }
  }
};
</script>

<style module lang="styl">
@import '../styles/colors.styl';

  .hero
    position relative
    background-color $black
    min-height 300px
    height 100vh
    max-width 100%
    overflow: hidden;
    padding 10px 16px
    color #f1f1f1
  
  .rains
    height 100%
    width 100%
    position absolute
    overflow hidden
    bottom 0
    top 0
  
  .title
    cursor pointer
    height 0
    z-index 2
    position absolute
    text-transform uppercase
    top 40%
    left 40%
    text-align center
    font-family 'Aldo the Apache'
    transition left 1s ease-out, font-size 1s ease-out 

    h1
      font-size 72px
      font-weight 800
      line-height 1
      color var(--offwhite)
</style>
