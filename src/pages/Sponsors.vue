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
          name: "Nitin Agrawal",
          company: "Google",
          portfolio: "Software",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/nitin-agrawal-sys/",
          photoUrl: "assets/alums/Nitin_Agrawal.jpeg"
        },
        {
          name: "Pranay Arya",
          company: "Bank of America",
          portfolio: "VP, Finance Manager - Enterprise Capital Management",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/pranay-arya-20aa6343",
          photoUrl: "assets/alums/Pranay_Arya.jpeg"
        },
        {
          name: "Abhay",
          company: "Oracle india pvt ltd",
          portfolio: "Director development",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/abhay-kumar-89433683",
          photoUrl: "assets/alums/Abhay.jpg"
        },
        {
          name: "Himanshu Bhalla",
          company: "Intel",
          portfolio: "Software Architect at Intel",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/hbhalla",
          photoUrl: "assets/alums/Himanshu_Bhalla.jpg"
        },
        {
          name: "Sudeep Ghosh",
          company: "Microsoft",
          portfolio: "Software developer",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/sudeepkghosh",
          photoUrl: "assets/alums/Sudeep_Ghosh.jpg"
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
          name: "Prashant Joshi",
          company: "SITA",
          portfolio: "Lead Analyst in SITA",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/prashant-joshi-548b64158",
          photoUrl: "assets/alums/Prashant_Joshi.jpeg"
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
          name: "Animesh Pathak",
          company: "myKaarma",
          portfolio: "PhD from USC, ex-Research Scientist at Inria (France), Head of R&D and Engineering at myKaarma, President IBGAA",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/animeshpathak",
          photoUrl: "assets/alums/Animesh_Pathak.jpeg"
        },
        {
          name: "Manish Poddar",
          company: "Qualcomm",
          portfolio: "Software",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/manish-poddar-2381091",
          photoUrl: "assets/alums/Manish_Poddar.jpg"
        },
        {
          name: "Manoj Poddar",
          company: "IBM",
          portfolio: "Software",
          graduationYear: 2003,
          linkedin: "https://www.linkedin.com/in/manoj-poddar-6010721a5/",
          photoUrl: "assets/alums/Manoj_Poddar.jpg"
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
        },
        {
          name: "Dhirendra Trivedi",
          company: "Juniper Networks",
          portfolio: "Sr Staff Engineer",
          graduationYear: 2003,
          linkedin: "http://www.linkedin.com/in/dhirendra-trivedi-92a3001",
          photoUrl: "assets/alums/Dhirendra_Trivedi.jpeg"
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
