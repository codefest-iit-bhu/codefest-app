<template>
  <div :class="$style.root">
    <AppBar />
    <div :class="[$style.wrapper, $style[$mq]]">
      <div :class="$style.teamHero">
        <img src="/assets/team.svg" />
      </div>
      <SectionLayout
        v-for="(team, i) in teams"
        :key="i"
        :title="team.title | capitalize"
      >
        <carousel
          :scrollPerPage="false"
          paginationColor="#6F2232"
          paginationActiveColor="#4298a7"
          :perPageCustom="[
            [768, 3],
            [1400, 4],
            [600, 2],
            [300, 1],
          ]"
          :autoplay="true"
          :autoplayTimeout="5000"
          :autoplayHoverPause="true"
        >
          <slide v-for="(person, j) in team.people" :key="j">
            <div :class="$style.teamMember">
              <object
                :data="`/assets/team/${team.title}/${person.name}.jpg`"
                type="image/jpg"
              >
                <img src="/assets/team/member.png" />
              </object>
              <br />
              <div :class="$style.name">{{ person.name }}</div>
              <div :class="$style.position">{{ person.position }}</div>
              <div :class="$style.social">
                <a :href="person.email ? `mailto:${person.email}` : null">
                  <i class="far fa-envelope"></i>
                </a>
                <a v-if="person.website" :href="person.website" target="_blank">
                  <i class="fas fa-globe"></i>
                </a>
                <a v-if="person.fb" :href="person.fb" target="_blank">
                  <i class="fab fa-facebook"></i>
                </a>
              </div>
            </div>
          </slide>
        </carousel>
      </SectionLayout>
    </div>
    <Footer />
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");
const SectionLayout = () => import("@components/layouts/SectionLayout");
import { Carousel, Slide } from "vue-carousel";

export default {
  components: {
    AppBar,
    SectionLayout,
    Footer,
    Carousel,
    Slide,
  },
  filters: {
    capitalize: function(value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    },
  },
  data() {
    return {
      teams: [
        {
          title: "core",
          people: [
            {
              name: "Avi Chawla",
              position: "Convener",
              email: "avi.chawla.cse16@iitbhu.ac.in",
              fb: "https://www.facebook.com/avi.chawla.10",
            },
            {
              name: "Utkarsh Tripathi",
              position: "Co-Convener",
              email: "utkarsh.tripathi.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/utkarsh.tripathi.315",
            },
            {
              name: "Keshav Kumar",
              position: "Co-Convener",
              email: "keshav.kumar.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/kk3799",
            },
            {
              name: "Govinda Totla",
              position: "Festival Manager",
              email: "govinda.totla.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/govinda.totla.1",
            },
            {
              name: "Khush Chopra",
              position: "PR Head",
              email: "khush.chopra.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/KhushC",
            },
            {
              name: "Anay Agrawal",
              position: "Marketing Head/Treasurer",
              email: "anay.agrawal.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/anay.agrawwal",
            },
            {
              name: "Deepak Kumar Gour",
              position: "Events Head - Algorithmic Divison",
              email: "deepak.gour.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/deepak.gour.enigma27",
            },
            {
              name: "Suyash Shukla",
              position: "Events Head - AI Divison",
              email: "suyash.shukla.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/suyash2510",
            },
            {
              name: "Vaishnav Menon",
              position: "Tech-Coordinator",
              email: "vsreekanth.menon.cse16@iitbhu.ac.in",
              fb: "https://m.facebook.com/vaishnavsm",
            },
          ],
        },
        {
          title: "tech",
          people: [
            {
              name: "Shivansh Saini",
              position: "Tech Head",
              email: "shivansh.saini.cse17@iitbhu.ac.in",
              website: "https://shivanshs9.me/?utm_source=cf19",
              fb: "https://www.facebook.com/thefaker99",
            },
            {
              name: "Piyush Maurya",
              position: "Front-end Developer",
              email: "piyushkr.maurya.cse17@iitbhu.ac.in",
              fb: "http://www.facebook.com/piyushkrmaurya",
            },
            {
              name: "Prabhash Kumar",
              position: "Front-end Developer",
              email: "prabhashkr.cd.cse17@itbhu.ac.in",
              fb: "http://www.facebook.com/iamxlr8",
            },
            {
              name: "Amritansh Singhal",
              position: "Back-end Developer",
              email: "amritansh.singhal.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/amritansh.singhal.75",
            },
            {
              name: "Pranav Dalal",
              position: "Back-end Developer",
              email: "pranavd.cd.cse17@itbhu.ac.in",
              fb: "https://m.facebook.com/pranav.dalal.94",
            },
            {
              name: "Dipesh Kumar",
              position: "Front-end Developer & UI/UX Designer",
              email: "dipesh.kumar.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/dipesh.kumar.92",
            },
          ],
        },
        {
          title: "content",
          people: [
            {
              name: "Khushi Agrawal",
              position: "Head",
              email: "khushia.cd.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/khushi.agrawal.733",
            },
            {
              name: "Hritwik Singhai",
              position: "Head",
              email: "hritwik.singhai.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/hritwiks",
            },
            {
              name: "Neeraj Alavelli",
              position: "Coordinator",
              email: "avenkata.neeraj.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/Neeraj.alavelli",
            },
          ],
        },
        {
          title: "design",
          people: [
            {
              name: "Dipesh Kumar",
              position: "Head",
              email: "dipesh.kumar.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/dipesh.kumar.92",
            },
            {
              name: "Amit",
              position: "Co-Head",
              email: "amit.student.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/dastanamit",
            },
            {
              name: "Shivam Tomar",
              position: "Co-Head",
              email: "shivam.tomar.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/shivam.tomar.921",
            },
            {
              name: "P. Radha Krishna",
              position: "Designer",
              email: "pradha.krishna.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/Radha.Krishna.2308",
            },
            {
              name: "Naman Talaycha",
              position: "Designer",
              email: "naman.talaycha.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/Namatalaycha10",
            },
          ],
        },
        {
          title: "publicity",
          people: [
            {
              name: "Abhinav Raj",
              position: "Head",
              email: "abhinav.raj.cse16@itbhu.ac.in",
              fb: "No FB",
            },
            {
              name: "Aditi Agarwal",
              position: "Co - Head",
              email: "aditia.cd.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/aditi.agarwal.311493",
            },
            {
              name: "Janhavi Gupta",
              position: "Co - Head",
              email: "janhavig.cd.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/janhavigupta007",
            },
            {
              name: "Rahul Chaturvedi",
              position: "Co - Head",
              email: "rahul.chaturvedi.cse17@iitbhu.ac.in",
              fb: "https://www.facebook.com/rahulchaturvedi24",
            },
            {
              name: "Pushpendra Kumar",
              position: "Co - Head",
              email: "pushpendra.kvaishya.cse17@itbhu.ac.in",
              fb: "https://m.facebook.com/pushpendra.bais.75?ref=bookmarks",
            },
            {
              name: "Khushi Agrawal",
              position: "Publicity Co-ordinator",
              email: "khushia.cd.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/khushi.agrawal.733",
            },
          ],
        },
        {
          title: "events",
          people: [
            {
              name: "Himanshu Singh",
              position: "Manthan",
              email: "himanshu.singh.cse16@itbhu.ac.in",
              fb: "https://m.facebook.com/hitman623",
            },
            {
              name: "Deepak Kumar Gour",
              position: "Manthan",
              email: "deepak.gour.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/deepak.gour.enigma27",
            },
            {
              name: "Bhavy Jain",
              position: "Mathmania",
              email: "bhavy.jain.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/bhavy.jain.94",
            },
            {
              name: "Naveen Punjabi",
              position: "Perplexed",
              email: "naveen.punjabi.cse16@iitbhu.ac.in",
              fb: "http://www.facebook.com/naveen.punjabi31",
            },
            {
              name: "Dhruv Rastogi",
              position: "Perplexed",
              email: "dhruv.rastogi.cse16@iitbhu.ac.in",
              fb: "https://www.facebook.com/dhruvrastogi21",
            },
            {
              name: "Abhinav Gupta",
              position: "Linguipedia",
              email: "abhinav.gupta.cse16@itbhu.ac.in",
              fb: "http://www.facebook.com/abhigupta768",
            },
            {
              name: "Avi Chawla",
              position: "Linguipedia",
              email: "avi.chawla.cse16@iitbhu.ac.in",
              fb: "https://www.facebook.com/avi.chawla.10",
            },
            {
              name: "Suyash Shukla",
              position: "Vista",
              email: "suyash.shukla.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/suyash2510",
            },
            {
              name: "Anurag Tyagi",
              position: "Enigma",
              email: "anurag.tyagi.cse16@itbhu.ac.in",
              fb: "https://m.facebook.com/anurag.7786995671",
            },
            {
              name: "Shreyansh Singh",
              position: "Capture the Flag",
              email: "shreyansh.singh.cse16@iitbhu.ac.in",
              fb: "https://www.facebook.com/shreyansh26.singh",
            },
            {
              name: "Apurv Jain",
              position: "Capture the Flag",
              email: "apurv.jain.cse16@iitbhu.ac.in",
              fb: "https://www.facebook.com/profile.php?id=100015115573049",
            },
          ],
        },
        {
          title: "marketing",
          people: [
            {
              name: "Anay Agrawal",
              position: "Head",
              email: "anay.agrawal.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/anay.agrawwal",
            },
            {
              name: "Tushar Khustule",
              position: "Co-Head",
              email: "ktushar.sanjay.cse16@itbhu.ac.in",
              fb: "https://www.facebook.com/tushar.sk.17",
            },
            {
              name: "Aditi Agarwal",
              position: "Member",
              email: "aditia.cd.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/aditi.agarwal.311493",
            },
            {
              name: "Hritwik Singhai",
              position: "Member",
              email: "hritwik.singhai.cse17@itbhu.ac.in",
              fb: "https://www.facebook.com/hritwiks",
            },
          ],
        },
      ],
    };
  },
};
</script>

<style module lang="stylus">

@require '~@styles/anims';

.wrapper {
  width: 80%;
  margin: 0 auto;
  padding: 50px 0;
  z-index: 1;
  position: relative;
  font: 500 18px 'Quicksand';
  font-kerning: auto;

  .heading {
    text-align: center;
    color: $waterloo;
    font-family: 'Aldo the Apache';
    padding: 12px 0;
    letter-spacing: 2px;
    $font-size: 64px;
    margin-top: 144px;

    ~/.lg ^[1..-1], ~/.xl ^[1..-1], ~/.xxl ^[1..-1] {
      padding-top: 36px;
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1], ~/.md ^[1..-1] {
      margin-top: 72px;
    }

    ~/.xs ^[1..-1] {
      $font-size: 52px;
    }
  }

  .line {
    height: 3px;
    border: none;
    background-image: linear-gradient(to right, $black, alpha($waterloo, 0.7), $black);
  }

  .teamHero {
    text-align: center;
    padding-top: 200px;
    padding-bottom: 150px;
    width: 800px;
    margin: auto;

    ~/.xs ^[1..-1] {
      width: 260px;
      padding-top: 100px;
      padding-bottom: 0;
    }

    ~/.sm ^[1..-1] {
      width: 400px;
      padding-top: 100px;
      padding-bottom: 0;
    }

    ~/.md ^[1..-1] {
      width: 500px;
      padding-top: 100px;
      padding-bottom: 50px;
    }

    ~/.md ^[1..-1] {
      width: 650px;
      padding-top: 150px;
      padding-bottom: 50px;
    }
  }

  .teamMember {
    text-align: center;
    padding: 40px 0;
    width: 250px;
    margin: 50px auto 25px;
    border-top: 4px solid $waterloo;
    border-bottom: 4px solid $waterloo;
    border-radius: 100px 0 100px 0;

    img, object {
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

    .position {
      $font-size: 14px;
      margin: 10px auto;
    }

    .social i {
      margin: 8px;
      $font-size: 16pt;

      &:hover {
        color: $limeade;
      }
    }

    ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
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
