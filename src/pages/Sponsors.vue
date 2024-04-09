<template>
  <div :class="$style.root">
    <AppBar :currentPage="'sponsors'" @scrollTop="scrollToTop" />
    <main :class="$style.wrapper">
      <!-- Heading -->
      <h1 :class="[$style.sectionTitle, $style[$mq], tooLong]">Sponsors</h1>
      <div :class="$style.intro">
          Experience the dynamic collaboration of technology and innovation at CodeFest'24, 
          generously supported by the esteemed alumni network of the 2003 Computer Science 
          and Engineering cohort from IIT (BHU) Varanasi. Join us as we celebrate their enduring 
          legacy and pioneering spirit in shaping the future of coding excellence.
      </div>

      <!-- Soponsors -->
      <SponsorCard :style="{'margin-top':'50px'}" :items="alumniData" />
      
    </main>
    <Footer />
  </div>
</template>

<script>
const AppBar = () => import("@components/Menu/AppBar");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const ResponsiveTwoColumnLayout = () => import("@components/layouts/ResponsiveTwoColumnLayout");
const Footer = () => import("@components/Footer");
const SponsorCard = () => import("@components/SponsorCard");

export default {
  components: {
    AppBar,
    SectionLayout,
    ResponsiveTwoColumnLayout,
    SponsorCard,
    Footer,
  },
  data() {
    return {
      alumniData: [
        {
          name: "Himanshu Bhalla",
          company: "Intel",
          portfolio: "Software Architect at Intel",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/hbhalla/?originalSubdomain=in",
          photoUrl: "assets/alums/Himanshu_Bhalla.jpg"
        },
        {
          name: "Vikas Gupta",
          company: "Broadcom",
          portfolio: "Principal Software Engineer at Broadcom",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/vikas-gupta-43309317?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
          photoUrl: "assets/alums/Vikas_Gupta.jpg"
        }, 
        {
          name: "Ajeet Kumar",
          company: "Microsoft",
          portfolio: "Microsoft",
          graduationYear: 2003,
          linkedin: "https://wwww.linkedin.com/in/ajeet-kumar-1995862",
          photoUrl: "assets/alums/Ajeet_Kumar.JPG"
        },
        {
          name: "Pawan Kumar",
          company: "Microsoft",
          portfolio: "Software Engineer at Microsoft",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/pawan-kumar-47bbba8/",
          photoUrl: "assets/alums/Pawan_kumar.jpg"
        },
        {
          name: "Vivek Lakwal",
          company: "SAP",
          portfolio: "Solution Architect at SAP",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/vivek-lakwal-2073096/?originalSubdomain=in",
          photoUrl: "assets/alums/vivek_lakwal.png"
        },
        {
          name: "Kamlesh Madheshiya",
          company: "Cadence Design Systems",
          portfolio: "Sr Eng Group Director at Cadence Design Systems",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/kamleshmadheshiya",
          photoUrl: "assets/alums/Kamlesh_Madheshiya.jpg"
        },
        {
          name: "Dheerendra Vikram Pandey",
          company: "Pan Science Innovations",
          portfolio: "MD and Group Chief Technology Officer at Pan Science Innovations",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/dheerendra-pandey-0152b982",
          photoUrl: "assets/alums/Dheerendra_Pandey.jpeg"
        },
        {
          name: "Mayur Srivastava",
          company: "Two Sigma Investments",
          portfolio: "Vice President, Architect in Storage group at Two Sigma Investments",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/mayur-s-basic",
          photoUrl: "assets/alums/Mayur_Srivastava.jpeg"
        },
        {
          name: "Atul Tiwari",
          company: "Citi",
          portfolio: "Citi",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/atul tiwari",
          photoUrl: "assets/alums/Atul_Tiwari.jpg"
        },
        {
          name: "Prabhat Tripathi",
          company: "Société Générale Securities",
          portfolio: "Director Cash Equities IT at Société Générale Securities",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/prabhat-tripathi-2b851313/?originalSubdomain=hk",
          photoUrl: "assets/alums/prabhat_tripathi.jpg"
        },
        {
          name: "Rajesh Kumar Tripathi",
          company: "Google",
          portfolio: "Google",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/rajesh-kumar-ucsb/",
          photoUrl: "assets/alums/Rajesh_Kumar.jpg"
        }]
    };
  },
  methods: {
    scrollToTop() {
      TweenLite.to(window, 1, { scrollTo: 0, ease: Power4.easeInOut });
    },
  },
};
</script>

<style module lang="stylus">

.wrapper {
  width: 80%;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  font: 500 18px 'Quicksand';
  padding: 100px 0;
}

h1.sectionTitle {
  font-family: 'Baloo Bhaina 2';
  color: var(--heading-color);
  letter-spacing: 2px;
  $font-size: 64px;
  margin-bottom: 0px;

  &.xs {
    $font-size: 52px;
  }

  ~/:nth-child(even) h1.sectionTitle {
    text-align: start;
  }

  ~/:nth-child(odd) h1.sectionTitle {
    text-align: end;
  }
}

.intro {
  font-size: 20px;
  text-align: left;
  max-width: 800px;
}

.root {
  height: 100%;
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
