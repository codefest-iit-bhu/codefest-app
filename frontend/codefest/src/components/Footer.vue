<template>
  <footer :class="$style.footer">
    <i :class="$style.heart"/>
    <span>Codefest' 19</span>
    
    <span :class="$style.socialIcons">
      <a>
        <img src="@assets/social_facebook.svg">
      </a>
      <a>
        <img src="@assets/social_twitter.svg">
      </a>
      <a>
        <img src="@assets/social_instagram.svg">
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
  height: 48px;

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
    margin-left: 5px;

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
