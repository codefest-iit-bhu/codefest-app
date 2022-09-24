<template>
  <div :class="[$style.heroContainer, $style[$mq]]">
    <ResponsiveTwoColumnLayout :isRightAbove="true">
      <div :class="$style.caHead" slot="left">
        <img src="#" />
        <span :class="$style.tagline">Imagine. Create. Iterate.</span>
        <span :class="$style.venue">
          <span :id="$style.loc">
            <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
          </span>
          <span :id="$style.sep">|</span>
          <span :id="$style.date">
            <i class="far fa-calendar-alt"></i> 23 - 25 August, 2019
          </span>
        </span>
        <h1>
          Want to be a part of the
          <span>BIGGEST</span> coding festival of the country ?
        </h1>
        <h3>
          Be part of
          <span>CODEFEST'20</span> by becoming our CAMPUS AMBASSADOR.
        </h3>
        <div :class="$style.link">
          <a
            href="https://forms.gle/BDcmVFr4K7o2GjRn9"
            :class="$style.linkText"
          >
            <h4>Register</h4>
          </a>
        </div>
      </div>
      <div :class="$style.caImage" slot="right">
        <img src="#" />
      </div>
    </ResponsiveTwoColumnLayout>
  </div>
</template>

<script>
const ResponsiveTwoColumnLayout = () =>
  import("@components/layouts/ResponsiveTwoColumnLayout");

export default {
  components: {
    ResponsiveTwoColumnLayout,
  },
};
</script>

<style module lang="stylus">
.heroContainer {
  width: 100%;
  text-align: center;

  .caImage {
    img {
      width: 440px;
      margin: auto;
      margin-bottom: 50px;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        width: 160px;
        margin-bottom: 0;
      }

      ~/.lg ^[1..-1], ~/.md ^[1..-1] {
        width: 280px;
      }
    }
  }

  .caHead {
    text-align: center;

    img {
      width: 400px;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1], ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        display: none;
      }
    }

    h1, h3 {
      text-align: center;
      font-family: 'Roboto Slab';
      font-weight: 600;
      margin: 48px 0;

      span {
        color: $waterloo;
        margin: 0 2px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        $font-size: 23px;
        margin: 24px 0;
      }

      ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        margin-top: 0;
      }

      ~/.md ^[1..-1] {
        $font-size: 30px;
      }
    }

    h3 {
      letter-spacing: 1.1px;
      text-align: center;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        $font-size: 16px;
        text-align: center;
      }

      ~/.md ^[1..-1] {
        $font-size: 18.72px;
      }
    }

    .link {
      margin: 0 auto 60px;
      width: 290px;
      height: auto;
      padding: 25px;
      border-radius: 50px;
      box-shadow: inset 0px 0px 20px $waterloo;
      animation: neon-box 1.5s ease-in-out infinite alternate;
      border: 2px solid $waterloo;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1], ~/.md ^[1..-1] {
        width: 220px;

        .linkText {
          text-align: center;

          h4 {
            margin: 0;
            $font-size: 21px;
          }
        }
      }

      a {
        text-decoration: none;
      }

      .linkText {
        text-align: center;
        font-family: 'Aldo the Apache';
        color: $waterloo;
        margin-top: 20px;
        display: inline;

        h4 {
          margin: 0;
          $font-size: 30px;
        }
      }
    }

    .tagline, .venue {
      height: 32px;
      display: block;
      text-align: center;
      margin: 8px auto;
      $font-size: 16px;
      font-weight: 600;
      font-family: 'Quicksand';

      #sep {
        margin: 0 8px;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1], ~/.md ^[1..-1], ~/.lg ^[1..-1] {
        display: none;
      }
    }
  }
}
</style>
