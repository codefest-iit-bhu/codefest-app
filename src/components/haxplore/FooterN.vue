<template>
  <footer :class="$style.footer">
    <div :class="$style.logo">
      <div   :class="$style.image">
        <img  src="@assets/haxplore/hax_white.svg" />
      </div>
      <p>Copyright © 2020 Haxplore</p>
    </div>
    <i :class="$style.heart" />
    <span :class="$style.socialIcons">
      Codefest' 20
      <a href="https://www.facebook.com/codefest/">
        <span class="fa-stack fa-lg">
          <!-- <i class="fa fa-circle-notch fa-stack-2x"></i> -->
          <i class="fab fa-facebook-f fa-stack-1x"></i>
        </span>
      </a>
      <a href="https://twitter.com/c0defest">
        <span class="fa-stack fa-lg">
          <!-- <i class="fa fa-circle-notch fa-stack-2x"></i> -->
          <i class="fab fa-twitter fa-stack-1x"></i>
        </span>
      </a>
      <a href="https://www.instagram.com/codefest.iitbhu">
        <span class="fa-stack fa-lg">
          <!-- <i class="fa fa-circle-notch fa-rotate fa-stack-2x"></i> -->
          <i class="fab fa-instagram fa-stack-1x"></i>
        </span>
      </a>
    </span>
  </footer>
</template>

<script>
export default {};
</script>

<style module lang="stylus">
.footer {
  $font-size: 10px;
  font-weight: 800;
  background: $mine-shaft;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-family: 'Quicksand';
  border-top: 2px solid rgba(34, 40, 49, 0.3);
  color: rgba($white, 0.65);
  justify-content: center;
  align-items: center;
  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
  margin-top: 20px;
  width: 100%;

  .logo {
    width: 100%;
    margin-top: 20px;


    .image {

      height: 50px;
      width: 170px;
      margin: 0 auto;
      position: relative;
    }

    img{
      position: absolute;
      margin: auto;
      top: -10px;
      right: -83px;
      width: 200%;
      height: 200%;
      
    }

    p {
      text-align: center;
      color: $white;
    }
  }

  span {
    font-family: 'Quicksand';

    a {
      color: inherit;
      transition: color var(--transition-duration);
    }
  }

  a {
    &:hover {
      color: rgba(255, 255, 255, 1);
    }
  }

  .socialIcons {
    margin-left: 10px;
    margin-bottom: 5px;

    a {
      position: relative;
      width: 30px;
      height: 30px;
    }
  }
}

.heart {
  width: 60px;
  height: 60px;
  display: inline;
  background: transparent url('~@assets/twitter_heart.png') no-repeat;
  background-size: 2900%;
  margin: 0 0;

  &:hover {
    background-position: right;
    animation: moveHeart 800ms steps(28) forwards;
  }
}

@keyframes moveHeart {
  0% {
    background-position: left;
  }

  50% {
    background-position: right;
  }

  100% {
    background-position: right;
  }
}
</style>
