<template>
  <footer :class="$style.footer">
    <i :class="$style.heart"/>
    <span>Codefest' 19</span>
    
    <span :class="$style.socialIcons">
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
      <a href="https://www.instagram.com/c0defest/?hl=en">
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
@import '../styles/colors.styl';

.footer {
  font-size: 60%;
  font-weight: 800;
  background: $outer-space;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-family: var(--font-header);
  border-top: 2px solid rgba(34, 40, 49, 0.3);
  color: rgba($white, 0.65);
  justify-content: center;
  align-items: center;
  display: flex;
  height: 52px;

  span {
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
  width: 40px;
  height: 40px;
  background: transparent url('@assets/twitter_heart.png') no-repeat;
  background-size: 2900%;
  margin: 0 -8px;

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
