<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.notFound">404</div>
    </main>
    <Footer/>
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");

export default {
  components: {
    AppBar,
    Footer
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.wrapper {
  width: 80%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  font-family: 'Roboto Mono';
  padding: 200px 20px 50px 20px;
  font-size: 18px;
}

.root {
  height: 100%;
}

.notFound {
  text-align: center;
  font-size: 7em;
  width: 20%;
  border: 2px solid $chartreuse;
  min-width: 100px;
  border-radius: 100%;
  margin: 20px auto 40px;
  animation: neon-box 1.5s ease-in-out infinite alternate;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
