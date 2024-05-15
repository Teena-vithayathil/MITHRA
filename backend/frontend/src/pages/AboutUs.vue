<template>
  <div :class="$style.aboutUs">
    <main :class="$style.mainFRAMEParent">
      <div :class="$style.mainFRAME">
        <div :class="$style.navigationBar1">
          <header :class="$style.buttonInstance" />
          <div :class="$style.mithraCarpoolingWrapper">
            <h3 :class="$style.mithraCarpooling">MITHRA Carpooling</h3>
          </div>
          <div :class="$style.button1">
            <div :class="$style.button1Child" />
            <div :class="$style.aboutUs1">About us</div>
          </div>
        </div>
        <img
          :class="$style.iconParkOutlineback"
          loading="lazy"
          alt=""
          src="/iconparkoutlineback.svg"
          @click="onIconParkOutlinebackClick"
        />
      </div>
      <section :class="$style.aboutUsWrapper">
        <h3 :class="$style.aboutUs2">
          <span :class="$style.aboutUsTxtContainer">
            <p :class="$style.aboutUs3">ABOUT US</p>
          </span>
        </h3>
      </section>
      <section :class="$style.welcomeToMithraWomensOnlWrapper">
        <div :class="$style.welcomeToMithraContainer">
          <p :class="$style.welcomeToMithra">
            Welcome to Mithra ,women’s only carpooling where we introduce a
            safer platform for women to share rides together .
          </p>
          <p :class="$style.blankLine">&nbsp;</p>
          <p :class="$style.blankLine1">&nbsp;</p>
          <p :class="$style.blankLine2">&nbsp;</p>
        </div>
      </section>
      <section :class="$style.expertTeamContainer">
        <div :class="$style.visionStatement">
          <img
            :class="$style.visionStatementChild"
            loading="lazy"
            alt=""
            src="/rectangle-39@2x.png"
          />
          <div :class="$style.ourVisionIsContainer">
            <p :class="$style.ourVisionIs">
              Our vision is to build a strong community by connecting women
              across Kerala.
            </p>
            <p :class="$style.ourServicesRange">
              Our services range from ride-sharing to product delivery services.
            </p>
            <p :class="$style.whatSetsUs">
              What sets us apart is our attention to detail and dedication to
              quality.
            </p>
            <p :class="$style.wePutOur">
              We put our hearts and souls into whatever we do.
            </p>
            <p :class="$style.ourJourneyIs">
              Our journey is guided by core values like integrity,innovation and
              excellence .
            </p>
            <p :class="$style.blankLine3">&nbsp;</p>
          </div>
        </div>
      </section>
      <div :class="$style.footerInstance">
        <div :class="$style.meetOurExpertContainer">
          <p :class="$style.meetOurExpert">Meet our expert Team</p>
          <p :class="$style.teenaVithayathilBackend">
            Teena Vithayathil -Backend Developer
          </p>
          <p :class="$style.jishaMariaJoseph">
            Jisha Maria Joseph- UI/UX Developer
          </p>
          <p :class="$style.himaSonyDatabaseDesigner">
            Hima Sony-Database Designer
          </p>
        </div>
      </div>
    </main>
    <footer :class="$style.footer">
      <div :class="$style.footerChild" />
    </footer>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "AboutUs",
    methods: {
      onIconParkOutlinebackClick() {
        this.$router.push("/home-page");
      },
    },
  });
</script>
<style module>
  .buttonInstance {
    height: 75px;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    top: 0px;
    right: 0px;
    left: 0px;
    background-color: var(--color-white);
  }
  .mithraCarpooling {
    margin: 0;
    align-self: stretch;
    height: 74.6px;
    position: relative;
    font-size: inherit;
    font-weight: 700;
    font-family: inherit;
    background: linear-gradient(90deg, #fb0f72, #fe8d08);
    -webkit-background-clip: text;
    background-clip: text; /* Fallback for non-webkit browsers */
    color: transparent;
    -webkit-text-fill-color: transparent;
    display: inline-block;
    flex-shrink: 0;
    white-space: nowrap;
    z-index: 1;
  }
  .mithraCarpoolingWrapper {
    width: 239.3px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-4xs) 0px 0px;
    box-sizing: border-box;
  }
  .button1Child {
    height: 100%;
    width: 100%;
    position: absolute;
    margin: 0 !important;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    border-radius: var(--br-3xl);
    background-color: var(--color-snow);
  }
  .aboutUs1 {
    height: 35.2px;
    flex: 1;
    position: relative;
    text-decoration: underline;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
  }
  .button1 {
    width: 133.9px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xs-6) var(--padding-smi-7) var(--padding-7xs-6)
      var(--padding-sm-7);
    box-sizing: border-box;
    position: relative;
    white-space: nowrap;
    z-index: 1;
    font-size: var(--font-size-sm);
    font-family: var(--font-chenla);
  }
  .navigationBar1 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 1440px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base) var(--padding-82xl) 0px;
    box-sizing: border-box;
    gap: 733.7px;
  }
  .iconParkOutlineback {
    position: absolute;
    top: 25px;
    left: 16px;
    width: 24px;
    height: 24px;
    cursor: pointer;
    z-index: 2;
  }
  .mainFRAME {
    align-self: stretch;
    height: 99.6px;
    position: relative;
  }
  .aboutUs3 {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .aboutUsTxtContainer {
    width: 100%;
  }
  .aboutUs2 {
    margin: 0;
    height: 105px;
    width: 658px;
    position: relative;
    font-size: inherit;
    line-height: 30px;
    font-weight: 400;
    font-family: inherit;
    display: flex;
    align-items: flex-end;
    flex-shrink: 0;
    max-width: 100%;
  }
  .aboutUsWrapper {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    padding: 0px var(--padding-xl) 0px 558px;
    box-sizing: border-box;
    max-width: 100%;
    text-align: left;
    font-size: 46px;
    color: var(--color-black);
    font-family: var(--font-irish-grover);
  }
  .welcomeToMithra {
    margin-block-start: 0;
    margin-block-end: 20px;
    line-height: 97.7%;
  }
  .blankLine {
    margin-block-start: 0;
    margin-block-end: 20px;
    line-height: 97.7%;
  }
  .blankLine1 {
    margin-block-start: 0;
    margin-block-end: 20px;
    font-size: var(--font-size-11xl);
    line-height: 10px;
  }
  .blankLine2 {
    margin: 0;
    font-size: var(--font-size-11xl);
    line-height: 10px;
  }
  .welcomeToMithraContainer {
    height: 130px;
    flex: 1;
    position: relative;
    display: inline-block;
    mix-blend-mode: color-burn;
    max-width: 100%;
  }
  .welcomeToMithraWomensOnlWrapper {
    width: 906px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 58px 77px;
    box-sizing: border-box;
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-16xl);
    color: var(--color-black);
    font-family: var(--font-space-grotesk);
  }
  .visionStatementChild {
    height: 531px;
    width: 538px;
    position: absolute;
    margin: 0 !important;
    right: 3px;
    bottom: -411px;
    border-radius: 265.5px;
    object-fit: cover;
    z-index: 1;
  }
  .ourVisionIs {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .ourServicesRange {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .whatSetsUs {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .wePutOur {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .ourJourneyIs {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .blankLine3 {
    margin: 0;
  }
  .ourVisionIsContainer {
    height: 201px;
    flex: 1;
    position: relative;
    line-height: 10px;
    display: inline-block;
    max-width: 100%;
    z-index: 2;
  }
  .visionStatement {
    width: 1359px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 0px 0px var(--padding-xl);
    box-sizing: border-box;
    position: relative;
    max-width: 100%;
  }
  .expertTeamContainer {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px var(--padding-8xs) 112px;
    box-sizing: border-box;
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-11xl);
    color: var(--color-black);
    font-family: var(--font-space-grotesk);
  }
  .meetOurExpert {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .teenaVithayathilBackend {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .jishaMariaJoseph {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .himaSonyDatabaseDesigner {
    margin: 0;
  }
  .meetOurExpertContainer {
    height: 230px;
    flex: 1;
    position: relative;
    line-height: 10px;
    display: inline-block;
    max-width: 100%;
  }
  .footerInstance {
    width: 838px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 47px;
    box-sizing: border-box;
    max-width: 100%;
    text-align: left;
    font-size: var(--font-size-11xl);
    font-family: var(--font-space-grotesk);
  }
  .mainFRAMEParent {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    max-width: 100%;
    text-align: center;
    font-size: var(--font-size-2xl);
    color: var(--color-black);
    font-family: var(--font-fahkwang);
  }
  .footerChild {
    align-self: stretch;
    flex: 1;
    position: relative;
    background: linear-gradient(90deg, #fb0f72, #f9a84a);
    max-width: 100%;
  }
  .footer {
    width: 1440px;
    height: 48px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    max-width: 103%;
    flex-shrink: 0;
  }
  .aboutUs {
    width: 100%;
    position: relative;
    background-color: var(--color-navajowhite);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 49px;
    line-height: normal;
    letter-spacing: normal;
  }

  @media screen and (max-width: 1200px) {
    .aboutUsWrapper {
      padding-left: 279px;
      box-sizing: border-box;
    }
  }
  @media screen and (max-width: 1150px) {
    .aboutUs2 {
      font-size: 37px;
      line-height: 24px;
    }

    .welcomeToMithraContainer {
      font-size: var(--font-size-5xl);
    }

    .welcomeToMithraWomensOnlWrapper {
      padding-left: var(--padding-10xl);
      padding-right: var(--padding-10xl);
      box-sizing: border-box;
    }

    .ourVisionIsContainer {
      font-size: var(--font-size-5xl);
      line-height: 8px;
    }

    .meetOurExpertContainer {
      font-size: var(--font-size-5xl);
      line-height: 8px;
    }

    .footerInstance {
      padding-left: var(--padding-4xl);
      padding-right: var(--padding-4xl);
      box-sizing: border-box;
    }
  }
  @media screen and (max-width: 750px) {
    .aboutUsWrapper {
      padding-left: 139px;
      box-sizing: border-box;
    }

    .aboutUs {
      gap: 24px;
    }
  }
  @media screen and (max-width: 450px) {
    .aboutUs2 {
      font-size: 28px;
      line-height: 18px;
    }

    .aboutUsWrapper {
      padding-left: var(--padding-xl);
      box-sizing: border-box;
    }

    .welcomeToMithraContainer {
      font-size: var(--font-size-lg);
    }

    .ourVisionIsContainer {
      font-size: var(--font-size-lg);
      line-height: 6px;
    }

    .meetOurExpertContainer {
      font-size: var(--font-size-lg);
      line-height: 6px;
    }
  }
</style>
