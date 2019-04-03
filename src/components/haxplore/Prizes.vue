<template>
  <SectionLayout title="Prizes" id="prizes">
    <div :class="[$style.wrapper, $style[$mq]]">
      <div :class="$style.prizesContainer">
        <CardLayout :class="$style.prize__first" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-first.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Rs 50, 000</h2>
            <h4>First Prize</h4>
          </span>
        </CardLayout>
        <CardLayout :class="$style.prize__second" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-second.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Rs 30, 000</h2>
            <h4>Second Prize</h4>
          </span>
        </CardLayout>
        <CardLayout :class="$style.prize__third" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-third.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Rs 20, 000</h2>
            <h4>Third Prize</h4>
          </span>
        </CardLayout>
        <CardLayout :class="$style.prize__fourth" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-third.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Kindle</h2>
            <h4>Fourth Prize</h4>
          </span>
        </CardLayout>
        <CardLayout :class="$style.prize__fifth" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-third.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Echo Dot</h2>
            <h4>Fifth Prize</h4>
          </span>
        </CardLayout>
        <CardLayout :class="$style.prize__consolation" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-third.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Zebronics goodies</h2>
            <h4>6th, 7th & 8th Prize</h4>
          </span>
        </CardLayout>

        <CardLayout :class="$style.prize__girls" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-third.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Rs 5, 000</h2>
            <h4>Best All girls</h4>
          </span>
        </CardLayout>
        <CardLayout :class="$style.prize__bhu" :extraCardClass="$style.whiteCard">
          <img src="@assets/haxplore/prize-third.svg" slot="header">
          <span :class="$style.txt" slot="content">
            <h2>Rs 5, 000</h2>
            <h4>Best IIT (BHU)</h4>
          </span>
        </CardLayout>
      </div>
      <CardLayout :class="$style.benefits" :extraCardClass="$style.whiteCard">
        <p slot="header">
          HaXplore is going to be the ultimate pit-stop for developers. From taking care of your accomodation to providing you with savoury treats; food facilities and refreshments throughout the competition. Don't worry about your travel costs as well, we'll have them covered for you!
          And even if you don't win anything, fret not my friend! You'll go home with loads of goodies, a lot of experience and memories for a lifetime.
        </p>
      </CardLayout>
    </div>
  </SectionLayout>
</template>

<script>
import SectionLayout from "@components/layouts/SectionLayout";
import GridLayout from "@components/layouts/GridLayout";
import CardLayout from "@components/layouts/CardLayout";

export default {
  components: {
    SectionLayout,
    GridLayout,
    CardLayout
  },
  data() {
    return {};
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/mixins';

.wrapper {
  .prizesContainer {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    user-select: none;
    justify-content: center;

    .prize {
      &__first {
        order: 0;
        flex: 1 1 calc((100% / 3));
        height: 300px;

        ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
          order: -1;
          flex: 1 1 100%;
        }
      }

      &__second {
        order: -1;
        flex: 1 1 calc((100% / 4));
        height: 250px;

        ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
          flex: 1 1 calc((100% / 2));
        }
      }

      &__third {
        order: 0;
        flex: 1 1 calc((100% / 4));
        height: 250px;

        ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
          flex: 1 1 calc((100% / 2));
        }
      }

      &__fourth, &__fifth, &__consolation {
        flex: 1 1 calc((100% / 3));
        height: 250px;
      }

      &__girls, &__bhu {
        flex: 0 1 calc((100% / 2.5));
        height: 250px;
      }
    }

    img {
      width: 100%;
      height: 100%;
      padding: 20px 0;
    }

    .txt {
      width: 100%;
      text-align: center;
      font-family: 'Roboto Slab';

      h2, h4 {
        margin: 0.5em;
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        h2 {
          font-size: 21px;
        }
      }
    }
  }

  .whiteCard {
    width: 90%;
    height: 90%;
    box-shadow: 0 0 10px $chartreuse;
    border-radius: 5px;

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 95%;
    }
  }

  .benefits .whiteCard {
    padding: 0 25px;
  }
}
</style>
