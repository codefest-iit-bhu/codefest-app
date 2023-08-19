<template>
  <div :class="$style.root">
    <AppBar />
    <main :class="$style.wrapper">
      <div :class="$style.back - circle">
        <div :class="$style.circle">404</div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");

export default {
  components: {
    AppBar,
    Footer,
  },
};
</script>

<style module lang="stylus">

@require '~@styles/anims';

.wrapper {
  width: 80%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  padding: 200px 20px 50px 20px;
  $font-size: 18px;
}

.root {
  height: 100%;
}

.circle {
  text-align: center;
  width: 360px;
  height: 360px;
  border-radius: 200px;
  margin: auto;
  animation: timeline-border-full 1.5s ease-in-out infinite alternate;
  color: $waterloo;
  font-family: 'Aldo the Apache';
  $font-size: 160px;
  font-weight: 600;
  padding: 100px 0;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
