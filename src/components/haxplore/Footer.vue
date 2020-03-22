<template>
  <footer :class="$style.footer">
    <div :class="$style.container">
      <div :class="$style.logo">
        <img src="@assets/haxplore/logo-text.svg">
      </div>

      <div :class="$style.content">
        <span>
          Copyright 2019 Haxplore | Codefest' 19
          <i :class="$style.heart"></i>
        </span>
      </div>

      <div :class="$style.social">
        <ul>
          <li>
            <a href="https://www.facebook.com/codefest/">
              <span class="fa-stack fa-lg">
                <i class="fab fa-facebook-f fa-stack-1x"></i>
              </span>
            </a>
          </li>
          <li>
            <a href="https://twitter.com/c0defest">
              <span class="fa-stack fa-lg">
                <i class="fab fa-twitter fa-stack-1x"></i>
              </span>
            </a>
          </li>
          <li>
            <a href="https://www.instagram.com/c0defest/?hl=en">
              <span class="fa-stack fa-lg">
                <i class="fab fa-instagram fa-stack-1x"></i>
              </span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.footer {
  font-size: 16px;
  font-weight: 800;
  background: rgba($mine-shaft, 0.8);
  letter-spacing: 0.5px;
  text-transform: uppercase;
  font-family: var(--font-header);
  border-top: 2px solid rgba(34, 40, 49, 0.3);
  color: rgba($black, 0.65);
  margin-top: 20px;
  height: 160px;
  width: 100%;
  bottom: 0;

  .container {
    width: 80%;
    height: 60px;
    margin: 0 auto;
    margin-top: 50px;
    display: flex;
    flex-flow: row;
    justify-content: space-between;

    .logo {
      order: 0;
      height: 60px;
      width: 468px;
    }

    .content {
      order: 1;
      width: 400px;
      font-size: 16px;
      padding-top: 22px;
      font-family: 'Quicksand';
      text-align: center;

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
    }

    .social {
      order: 2;

      a {
        position: relative;
        width: 30px;
        height: 30px;

        span {
          font-family: 'Quicksand';
          color: rgba($black, 0.65);

          i {
            color: inherit;
            transition: color var(--transition-duration);
          }
        }
      }

      a:hover {
        span {
          i {
            color: $black;
          }
        }
      }

      ul {
        li {
          display: inline;
        }
      }
    }
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
