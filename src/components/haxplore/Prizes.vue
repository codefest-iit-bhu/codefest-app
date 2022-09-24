<template>
  <SectionLayout title="Prizes" id="prizes">
    <div :class="[$style.wrapper, $style[$mq]]">
      <div :class="$style.prizesContainer">
        <CardLayout
          :class="$style.prize__first"
          :extraCardClass="$style.whiteCard"
        >
          <img src="@assets/haxplore/prize-first.svg" slot="header" />
          <span :class="$style.txt" slot="content">
            <h2>Rs 15, 000</h2>
            <h4>First Prize</h4>
          </span>
        </CardLayout>
        <CardLayout
          :class="$style.prize__second"
          :extraCardClass="$style.whiteCard"
        >
          <img src="@assets/haxplore/prize-second.svg" slot="header" />
          <span :class="$style.txt" slot="content">
            <h2>Rs 10, 000</h2>
            <h4>Second Prize</h4>
          </span>
        </CardLayout>
        <CardLayout
          :class="$style.prize__third"
          :extraCardClass="$style.whiteCard"
        >
          <img src="@assets/haxplore/prize-third.svg" slot="header" />
          <span :class="$style.txt" slot="content">
            <h2>Rs 5, 000</h2>
            <h4>Third Prize</h4>
          </span>
        </CardLayout>
        <CardLayout
          :class="$style.prize__consolation"
          :extraCardClass="$style.whiteCard"
        >
          <img src="@assets/haxplore/prize-consolation.png" slot="header" />
          <span :class="$style.txt" slot="content">
            <h2>Exclusive goodies</h2>
            <h4>4th, 5th & 6th Prize</h4>
          </span>
        </CardLayout>

        <CardLayout
          :class="$style.prize__girls"
          :extraCardClass="$style.whiteCard"
        >
          <img src="@assets/haxplore/prize-girls.svg" slot="header" />
          <span :class="$style.txt" slot="content">
            <h2>Rs 5, 000</h2>
            <h4>Best All girls</h4>
          </span>
        </CardLayout>
      </div>
    </div>
  </SectionLayout>
</template>

<script>
const SectionLayout = () => import("@components/layouts/SectionLayout");
const GridLayout = () => import("@components/layouts/GridLayout");
const CardLayout = () => import("@components/layouts/CardLayout");

export default {
  components: {
    SectionLayout,
    GridLayout,
    CardLayout,
  },
  data() {
    return {};
  },
};
</script>

<style module lang="stylus">
.wrapper {
  .prizesContainer {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    user-select: none;
    justify-content: center;

    img {
      width: 100%;
      height: 100%;
      padding: 20px 0;
      margin: 0 auto;
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
          $font-size: 21px;
        }
      }
    }

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

      &__consolation, &__girls, &__bhu {
        flex: 0 1 calc((100% / 2.5));
        height: 250px;

        ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
          flex: 0 1 calc((100% / 2));
        }
      }

      &__consolation {
        img {
          width: unset;
        }
      }
    }
  }

  .whiteCard {
    width: 90%;
    height: 90%;
    border-radius: 5px;
    text-align: center;

    // color: $waterloo;
    // background: transparent;
    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 95%;
    }
  }

  .assured {
    background: transparent;
    margin-top: 36px;
    box-shadow: 0 0 10px $waterloo inset;
    border-radius: 10px;

    p {
      padding: 0 20px;
      background: transparent;
      color: $white;
    }
  }

  .benefits .whiteCard {
    padding: 0 25px;
  }
}
</style>
