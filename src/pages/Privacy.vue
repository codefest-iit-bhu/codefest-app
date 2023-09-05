<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar :shouldShowSideNavigation="false" />
    <main :class="$style.wrapper">
      <SectionLayout title="Our Privacy Policy" id="about">
	    <p>One of our main priorities at CodeFest is the privacy of our visitors. This Privacy Policy document below contains types of information that are collected and recorded by CodeFest and how we use it.<br /><br />

	    This Privacy Policy applies only to our online activities and is valid for visitors to our website with regards to the information that they shared and/or collect in CodeFest. This policy is not applicable to any information collected offline or via channels other than this website.</p>

      <br />
      <h2>Consent</h2>
      <p> By using our website, you hereby consent to our Privacy Policy and agree to its terms. The Personal Information that we collect is used for providing and improving the Service. We will not use or share your information with anyone except as described in this Privacy Policy. </p>

      <br />
      <h2>Information we collect</h2>
      <p> The personal information that you are asked to provide, and the reasons why you are asked to provide it, will be made clear to you at the point we ask you to provide your personal information.</p>

      <ul>
          <li>We collect your personal information (e.g. name, email address, phone, gender) to provide you better personalized services.</li>
          <li>We collect information related to your education(eg Your school/institute name and year of study).</li>
          <li>A user if they want may also provide their resume and profile handles on various programming websites( eg. Codeforces, HackerRank, etc)</li>
      </ul>

      <br />
      <h2>Information collected by external services.</h2>
      <p> The app does use third-party services that may collect information used to identify you. Link to the privacy policy of third party service providers used by the app:</p>

      <ul>
          <li><a href="https://policies.google.com/privacy/">Google </a></li>
          <li><a href="https://www.facebook.com/about/privacy/">Facebook </a></li>
          <li><a href="https://enterprise.github.com/privacy">Github </a></li>
      </ul>

      <br />
      <h2>How we use your information.</h2>
      <p>We use the information we collect in various ways, including:</p>

      <ul>
          <li>Provide, operate, improve, personalize and maintain our website.</li>
          <li>Communicate with you directly to provide you with updates and other information relating to the website, and for marketing and promotional purposes.</li>
          <li>Send you emails regarding upcoming events in which you have registered.</li>
          <li>Your education information helps us to confirm your identity and check if you are eligible for prizes as might be specified for the events you participate in.</li>
          <li>Providing us your resume and handles on websites is completely optional. This data will be used for providing employment opportunities to the user.</li>
      </ul>

      <br />
      <h2>Cookies and Analytics.</h2>
      <p>Like any other website, CodeFest uses 'cookies'. These cookies are used to store information including visitors' preferences, and the pages on the website that the visitor accessed or visited. The information is used to optimize the users' experience by customizing our web page content based on visitors' browser type and/or other information.</br></br>
      CodeFest also uses cookies from third-party partners such as Google for the purpose of analysis of visitor behavior and demographic information to improve the visitor experience.</br></br>
      You can choose to disable cookies through your individual browser options. To know more detailed information about cookie management with specific web browsers, it can be found at the browsers' respective websites. For more general information on cookies, please read "What Are Cookies".</p>

      <br />
      <h2>Third-Party Privacy Policies.</h2>
      <p>CodeFest's Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies of these third-party ad servers for more detailed information. It may include their practices and instructions about how to opt-out of certain options.
      </p>

      <br />
      <h2>Children's Information.</h2>
      <p>Another part of our priority is adding protection for children while using the internet. We encourage parents and guardians to observe, participate in, and/or monitor and guide their online activity.</br></br>
      CodeFest does not knowingly collect any Personal Identifiable Information from children under the age of 13. If you think that your child provided this kind of information on our website, we strongly encourage you to contact us immediately and we will do our best efforts to promptly remove such information from our records.
      </p>

      <br />
      <h2>Changes to This Privacy Policy.</h2>
      <p>We may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new Privacy Policy on this page. These changes are effective immediately after they are posted on this page.
      </p>

      <br />
      <h2>Contact us.</h2>
      <p>If you have any questions or suggestions about our Privacy Policy, do not hesitate to contact us.
      </br></br>
      Reach us through mail at <a href = "mailto: codefest@iitbhu.ac.in">codefest@iitbhu.ac.in</a>
      </br></br>
      You may even reach us at <b>CES, Department of Computer Science and Engineering, IIT(BHU), Varanasi, Uttar Pradesh-221005, India.</b></p>

	  </SectionLayout>

    </main>
    <Footer />
  </div>
</template>

<script>
import API from "@js/api";

const AppBar = () => import("@components/Menu/AppBar");
const SectionLayout = () => import("@components/layouts/SectionLayout");
const Footer = () => import("@components/Footer");

export default {
  components: {
    AppBar,
    SectionLayout,
    Footer,
  },
  data() {
    return {
    };
  },
  created() {
  },
};
</script>

<style module lang="stylus">

@require '~@styles/anims';

.root {
  height: 100%;

  .wrapper {
    width: 80%;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    font: 500 18px 'Quicksand';
    padding: 100px 0;
  }

  ul {
    list-style-position: inside;
  }

  li{
    padding: 3px;
  }
}

@media screen and (max-width: 769px) {
  .wrapper {
    width: 90%;
  }
}
</style>
