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
    var code = "01{}-+=xyz*&%$<>?/\\89".split("");
    var font_size = 25;
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
      requestAnimationFrame(draw);
    }
    draw();
  }
};
</script>

<style module lang="stylus">
@import '../styles/colors.styl';
@import '../styles/anims.styl';

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
  width: 100%;
  z-index: 2;
  position: absolute;
  top: 35%;
  margin: auto;
  text-align: center;

  h1 {
    font-size: 144px;
    font-family: Ubuntu;
    font-weight: 300;
    animation: neon-text 1.5s ease-in-out infinite alternate;
  }

  h1 span {
    font-size: 180px;
    font-weight: 600;
    margin: 0;
    padding: 0;
  }

  h1 sup {
    font-size: 100px;
    font-weight: 300;
  }
}
</style>
