<template>
  <div :class="[$style.contactList, $style[$mq]]">
    <GridLayout
      :itemWidth="computedWidth"
      v-if="['md', 'lg', 'xl', 'xxl'].includes(this.$mq)"
    >
      <div
        :class="$style.teamMember"
        v-for="(contact, i) in this.contacts"
        :key="i"
        :slot="`items${i}`"
      >
        <img :src="contact.pic" />
        <br />
        <div :class="$style.name">{{ contact.name }}</div>
        <div :class="$style.email">{{ contact.email }}</div>
        <div :class="$style.phone">{{ contact.phone }}</div>
      </div>
    </GridLayout>
    <carousel
      :scrollPerPage="false"
      paginationColor="#57A300"
      paginationActiveColor="#86FF00"
      :perPageCustom="[
        [768, 3],
        [1400, 4],
        [600, 2],
        [300, 1],
      ]"
      :autoplay="true"
      :autoplayTimeout="5000"
      :autoplayHoverPause="true"
      v-else
    >
      <slide v-for="(contact, i) in this.contacts" :key="i">
        <div :class="$style.teamMember">
          <img :src="contact.pic" />
          <br />
          <div :class="$style.name">{{ contact.name }}</div>
          <div :class="$style.email">{{ contact.email }}</div>
          <div :class="$style.phone">{{ contact.phone }}</div>
        </div>
      </slide>
    </carousel>
  </div>
</template>
<script>
const GridLayout = () => import("@components/layouts/GridLayout");
import { Carousel, Slide } from "vue-carousel";

export default {
  components: {
    GridLayout,
    Carousel,
    Slide,
  },
  computed: {
    computedWidth() {
      return "300px";
    },
  },
  data() {
    return {
      contacts: [
        {
          name: "Abhinav Raj",
          email: "abhinav.raj.cse16@itbhu.ac.in",
          phone: "+91 8890921899",
          pic: "/assets/team/ca/Abhinav Raj.jpg",
        },
        {
          name: "Keshav Kumar",
          email: "keshav.kumar.cse16@itbhu.ac.in",
          phone: "+91 8004236173",
          pic: "/assets/team/ca/Keshav Kumar.jpg",
        },
        {
          name: "Rahul Chaturvedi",
          email: "rahul.chaturvedi.cse17@itbhu.ac.in",
          phone: "+91 7023210104",
          pic: "/assets/team/ca/Rahul Chaturvedi.jpg",
        },
        {
          name: "Rahul Pandey",
          email: "rahul.dpandey.cse17@itbhu.ac.in",
          phone: "+91 8299735398",
          pic: "/assets/team/ca/Rahul Pandey.jpg",
        },
      ],
    };
  },
};
</script>

<style module lang="stylus">
.contactList {
  .teamMember {
    text-align: center;
    padding: 40px 0;
    width: 300px;
    margin: 50px auto 25px;
    border-top: 4px solid $waterloo;
    border-bottom: 4px solid $waterloo;
    border-radius: 100px 0 100px 0;

    img {
      border-radius: 100%;
      border: 2px solid $waterloo;
      animation: timeline-border-green 1.5s ease-in-out infinite alternate;
      width: 200px;
      height: 200px;
      margin-bottom: 20px;
    }

    .name {
      font-family: 'Roboto Slab';
      font-weight: 600;
      letter-spacing: 1.05px;
    }

    .email, .phone {
      font-family: 'Quicksand';
      $font-size: 14px;
      padding: 10px 0 0 0;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
      width: 260px;
      padding: 25px 0;
      margin: 25px auto;
    }

    ~/.md ^[1..-1], ~/.lg ^[1..-1] {
      padding: 30px 0;
      margin: 25px auto 0;
    }
  }
}
</style>
