<template>
  <header ref="header" :class="$style.hero">
    <!-- <Nav /> -->
    <div :class="$style.title">
      <h1>Codefest'19</h1>
    </div>
    <canvas ref="rains" :class="$style.rains" ></canvas>
  </header>
</template>

<script>
import Nav from '@components/Nav';

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
    var columns = 2*c.width/font_size;
    var drops = [];
    for(var x = 0; x < columns; x++) drops[x] = 1;
    function draw(){
      ctx.fillStyle = "rgba(0, 0, 0, 0.03)";
      ctx.fillRect(0, 0, c.width, c.height);
      ctx.fillStyle = "#86ff00";
      ctx.font = font_size + "px Courier New";
      for(var i = 0; i < drops.length; i++){
        var text = code[Math.floor(Math.random()*code.length)];
        ctx.fillText(text, i*font_size, drops[i]*font_size);
        
        if(drops[i]*font_size > c.height && Math.random() > 0.975) drops[i] = 0;
        
        drops[i]++;
      }
    }
    setInterval(draw, 33);
  }
}
</script>

<style module lang="styl">
@import '../styles/colors.styl';

  .hero
    position relative
    background-color $black
    min-height 300px
    height 100vh
  
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
    position relative
    text-transform uppercase
    top calc(40% - 2px)
    text-align center
    font-family 'Aldo the Apache'
    h1
      font-size 72px
      font-weight 800
      line-height 1
      color var(--offwhite)
</style>
