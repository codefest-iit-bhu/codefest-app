<template>
  <div :class="[$style.contactList, $style[$mq]]">
    <GridLayout :itemWidth="computedWidth">
      <div :class="$style.card" v-for="(contact, i) in this.contacts" :key="i" :slot="`item${i}`">
        <div :class="$style.name">{{ contact.name }}</div>
        <div :class="$style.email">{{ contact.email }}</div>
        <div :class="$style.phone">{{ contact.phone }}</div>
      </div>
    </GridLayout>
  </div>
</template>
<script>
const GridLayout = () => import("@components/layouts/GridLayout");

export default {
  components: {
    GridLayout
  },
  computed: {
    computedWidth() {
      return "300px";
    }
  },
  data() {
    return {
      contacts: [
        {
          name: "Abhinav Raj",
          email: "abhinav.raj.cse16@itbhu.ac.in",
          phone: "+91 1234567890"
        },
        {
          name: "Rahul Chaturvedi",
          email: "rahul.chaturvedi.cse17@itbhu.ac.in",
          phone: "+91 1234567890"
        },
        {
          name: "Rahul Pandey",
          email: "rahul.deopandey.cse17@itbhu.ac.in",
          phone: "+91 8299735398"
        },
        {
          name: "Ashok Meena",
          email: "ashok.meena.cse17@itbhu.ac.in",
          phone: "+91 9205001742"
        }
      ]
    };
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';

.contactList {
  .card {
    width: 320px;
    height: 200px;
    background: $chartreuse;
    border-radius: 60px 0;
    padding: 40px 0;

    .name {
      padding-bottom: 20px;
      text-align: center;
      color: $black;
      line-height: 28px;
      font-size: 28px;
    }

    .email {
      padding-bottom: 16px;
    }

    .name, .email, .phone {
      font-family: 'Roboto Slab';
      font-weight: 600;
      text-align: center;
      color: $black;
      line-height: 28px;
      margin-left: auto;
      margin-right: auto;
    }
  }
}
</style>
