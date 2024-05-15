<template>
  <div :class="$style.stPage">
    <main :class="$style.fRAME">
      <img :class="$style.fRAMEChild" alt="" src="/rectangle-1@2x.png" />
      <section :class="$style.mithraBridgingDistancesContainer">
        <span :class="$style.mithraBridgingDistancesContainer1">
          <p :class="$style.mithra">
            <span :class="$style.mithra1">
              <span>Mithra</span>
            </span>
          </p>
          <p :class="$style.bridgingDistancesBuildingB">
            <span :class="$style.bridgingDistancesBuildingB1">
              <span>bridging distances, building bonds</span>
            </span>
          </p>
          <p :class="$style.yourMostTrusted">
            Your most trusted travel companion, women's exclusive
            carpooling community
          </p>
        </span>
      </section>
    </main>
    <div :class="$style.navigationBar1">
      <header :class="$style.name" />
      <div :class="$style.mithraCarpoolingWrapper">
        <h3 :class="$style.mithraCarpooling">MITHRA Carpooling</h3>
      </div>
      <div :class="$style.button1">
        <div :class="$style.button1Child" />
        <div :class="$style.aboutUs" @click="about">About us</div>
      </div>
    </div>
    <div :class="$style.footerComponent">
      <div :class="$style.clickableButtonWrapper">
        <div :class="$style.clickableButton">
          <div :class="$style.clickableButtonChild" />
          <button :class="$style.clickButton">
            <div :class="$style.clickButtonChild" />
            <div :class="$style.signUp" @click="signup">Sign Up</div>
          </button>
          <button :class="$style.clickButton1">
            <div :class="$style.clickButtonItem" />
            <div :class="$style.signUp1" @click="login">Login</div>
          </button>
        </div>
      </div>
      <footer :class="$style.footer">
        <div :class="$style.footerChild" />
      </footer>
    </div>
  </div>
</template>
<script >
  import { defineComponent } from "vue";
  export default defineComponent({
    name: "StPage",
    methods: {
      about() {
        this.$router.push({ name: "AboutUs" });
      },
      signup() {
        this.$router.push({ name: "SignupPage" });
      },
      login() {
        this.$router.push({ name: "LoginPage" });
      }
    },
  });
</script>
<style module>
  .fRAMEChild {
    height: 1034.5px;
    flex: 1;
    position: relative;
    border-radius: 1px;
    max-width: 100%;
    overflow: hidden;
    object-fit: cover;
  }
  .mithra1 {
    text-transform: uppercase;
    background: linear-gradient(180deg, #fb0f72, #fe8d08);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .mithra {
    margin-block-start: 0;
    margin-block-end: 8px;
  }
  .bridgingDistancesBuildingB1 {
    text-transform: uppercase;
    background: linear-gradient(180deg, #fb0f72, #fe8d08);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .bridgingDistancesBuildingB {
    margin-block-start: 0;
    margin-block-end: 8px;
    font-size: 50px;
  }
  .yourMostTrusted {
    margin: 0;
    font-size: 35px;
  }
  .mithraBridgingDistancesContainer1 {
    width: 100%;
  }
  .mithraBridgingDistancesContainer {
    height: 376px;
    width: 1276px;
    position: absolute;
    margin: 0 !important;
    top: 264.5px;
    left: 34px;
    font-weight: 700;
    font-family: var(--font-rambla);
    text-align: left;
    display: flex;
    align-items: center;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    z-index: 2;
    font-size: 80px;
    color: #6f0632;
  }
  .fRAME {
    width: 1384px;
    margin: 0 !important;
    position: absolute;
    top: 15.5px;
    left: 0px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    max-width: 100%;
  }
  .name {
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
    background-color: var(--color-snow-100);
  }
  .aboutUs {
    height: 35.2px;
    flex: 1;
    position: relative;
    text-decoration: underline;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    z-index: 1;
  }
  .button1 {
    width: 133.9px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xs-6) var(--padding-smi) var(--padding-7xs-6)
      var(--padding-sm-7);
    box-sizing: border-box;
    position: relative;
    white-space: nowrap;
    z-index: 1;
    font-size: var(--font-size-sm);
    font-family: var(--font-chenla);
  }
  .navigationBar1 {
    width: 1440px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-base) var(--padding-82xl) 0px;
    box-sizing: border-box;
    position: relative;
    gap: var(--gap-714xl-7);
    max-width: 104%;
    flex-shrink: 0;
    z-index: 1;
  }
  .clickableButtonChild {
    height: 249px;
    width: 564px;
    position: relative;
    border-radius: var(--br-31xl);
    background-color: var(--color-white);
    display: none;
    max-width: 100%;
  }
  .clickButtonChild {
    position: absolute;
    height: 100%;
    top: 0px;
    bottom: 0px;
    left: 12px;
    border-radius: var(--br-6xl);
    background-color: var(--color-sandybrown);
    width: 204px;
  }
  .signUp {
    position: absolute;
    top: 20px;
    left: 44px;
    font-size: var(--font-size-6xl);
    font-weight: 500;
    font-family: var(--font-cabin);
    color: var(--color-black);
    text-align: center;
    display: inline-block;
    width: 146px;
    height: 34px;
    white-space: nowrap;
    z-index: 1;
  }
  .clickButton {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    height: 70px;
    width: 216px;
    position: relative;
    border-radius: var(--br-3xs);
    z-index: 2;
  }
  .clickButtonItem {
    position: absolute;
    height: 100%;
    top: 0px;
    bottom: 0px;
    left: 12px;
    border-radius: var(--br-6xl);
    background-color: var(--color-sandybrown);
    width: 204px;
  }
  .signUp1 {
    position: absolute;
    top: 20px;
    left: 44px;
    font-size: var(--font-size-6xl);
    font-weight: 500;
    font-family: var(--font-cabin);
    color: var(--color-black);
    text-align: center;
    display: inline-block;
    width: 146px;
    height: 34px;
    z-index: 1;
  }
  .clickButton1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    height: 70px;
    width: 216px;
    position: relative;
    border-radius: var(--br-3xs);
    z-index: 2;
  }
  .clickableButton {
    width: 564px;
    border-radius: var(--br-31xl);
    background-color: var(--color-white);
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 104px var(--padding-sm) var(--padding-56xl);
    box-sizing: border-box;
    gap: 52px;
    max-width: 100%;
    z-index: 1;
  }
  .clickableButtonWrapper {
    width: 784px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    padding: 0px var(--padding-xl);
    box-sizing: border-box;
    max-width: 100%;
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
    max-width: 104%;
    flex-shrink: 0;
    z-index: 1;
  }
  .footerComponent {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 157px;
    max-width: 100%;
  }
  .stPage {
    width: 100%;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 494.4px;
    line-height: normal;
    letter-spacing: normal;
    text-align: center;
    font-size: var(--font-size-2xl);
    color: var(--color-black);
    font-family: var(--font-fahkwang);
  }

  @media screen and (max-width: 1200px) {
    .navigationBar1 {
      gap: var(--gap-348xl);
      padding-left: var(--padding-31xl);
      padding-right: var(--padding-31xl);
      box-sizing: border-box;
    }

    .footerComponent {
      gap: 78px;
    }

    .stPage {
      gap: 247px;
    }
  }
  @media screen and (max-width: 725px) {
    .mithraBridgingDistancesContainer {
      font-size: 28px;
    }
  }
  @media screen and (max-width: 650px) {
    .navigationBar1 {
      gap: var(--gap-164xl);
      padding-left: var(--padding-6xl);
      padding-right: var(--padding-6xl);
      box-sizing: border-box;
    }

    .clickableButton {
      flex-wrap: wrap;
      gap: 26px;
    }

    .footerComponent {
      gap: 39px;
    }

    .stPage {
      gap: 124px;
    }
  }
  @media screen and (max-width: 450px) {
    .mithraBridgingDistancesContainer {
      font-size: var(--font-size-2xl);
    }

    .navigationBar1 {
      gap: var(--gap-73xl);
    }

    .signUp {
      font-size: var(--font-size-xl);
    }

    .signUp1 {
      font-size: var(--font-size-xl);
    }

    .footerComponent {
      gap: var(--gap-xl);
    }

    .stPage {
      gap: 62px;
    }
  }
</style>
