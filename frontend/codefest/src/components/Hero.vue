<template>
  <header ref="header" :class="$style.hero">
    <div :class="$style.title">
      <h1 id="heroTitle">
        code
        <span>Fest</span>
        <sup>19</sup>
      </h1>
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
  }
};
</script>

<style module lang="stylus">
@import '../styles/colors.styl';

.hero {
  position: relative;
  background-color: $black;
  min-height: 300px;
  height: 100vh;
  max-width: 100%;
  overflow: hidden;
  padding: 10px 16px;
  color: #f1f1f1;
}

.rains {
  height: 100%;
  width: 100%;
  position: absolute;
  overflow: hidden;
  bottom: 0;
  top: 0;
}

.title {
  height: 30%;
  width: 50%;
  z-index: 2;
  position: absolute;
  top: 40%;
  margin-left: 25%;
  text-align: center;

  h1 {
    font-size: 144px;
    font-family: Ubuntu;
    font-weight: 300;
    -webkit-animation: neon 1.5s ease-in-out infinite alternate;
    -moz-animation: neon 1.5s ease-in-out infinite alternate;
    animation: neon 1.5s ease-in-out infinite alternate;
  }

  h1 span {
    font-size: 180px;
    font-weight: 500;
    margin: 0;
    padding: 0;
  }
}

@keyframes neon {
  from {
    text-shadow: 0 0 2.5px $white, 0 0 5px $white, 0 0 7.5px $white, 0 0 10px $chartreuse, 0 0 12.5px $chartreuse, 0 0 15px $chartreuse, 0 0 25px $chartreuse;
  }

  to {
    text-shadow: 0 0 1px $white, 0 0 2px $white, 0 0 3px $white, 0 0 4px $chartreuse, 0 0 5px $chartreuse, 0 0 6px $chartreuse, 0 0 10px $chartreuse;
  }
}
</style>
