<template>
  <div :class="$style.profileNotVerified">
    <div :class="$style.mainView">
      <div :class="$style.navigationBar1">
        <header :class="$style.navigationBar1Child" />
        <div :class="$style.button1" @click="onButton1ContainerClick">
          <div :class="$style.aboutUs" />
          <div :class="$style.aboutUs1">About us</div>
        </div>
        <div :class="$style.brand">
          <h3 :class="$style.mithraCarpooling">MITHRA Carpooling</h3>
        </div>
      </div>
      <div :class="$style.button11" @click="onButton1Container2Click">
        <div :class="$style.button1Child" />
        <div :class="$style.aboutUs2">Sign out</div>
      </div>
    </div>
    <section :class="$style.content">
      <div :class="$style.messageContainer">
        <div :class="$style.errorMessagePanel">
          <img
            :class="$style.sad1Icon"
            loading="lazy"
            alt=""
            src="/sad-1@2x.png"
          />
        </div>
        <h1 :class="$style.oopsYourProfile">
          OOPS!!! YOUR PROFILE HAS NOT BEEN VERIFIED!!!
        </h1>
      </div>
    </section>
    <footer :class="$style.footer">
      <div :class="$style.footer1" />
    </footer>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "ProfileNotVerified",
    methods: {
      onButton1ContainerClick() {
        this.$router.push({ name: "AboutUs" });
      },
      onButton1Container2Click() {
        this.$router.push({ name: "StPage" });
      },
    },
  });
</script>
<style module>
  .navigationBar1Child {
    width: 100%;
    height: 75px;
    position: absolute;
    margin: 0 !important;
    top: 0px;
    right: 0px;
    left: 0px;
    background-color: #fff;
  }
  .aboutUs {
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
    flex: 1;
    position: relative;
    text-decoration: underline;
    z-index: 1;
  }
  .button1 {
    width: 133.9px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xs-6) var(--padding-smi-7) var(--padding-mini-8)
      var(--padding-sm-7);
    box-sizing: border-box;
    position: relative;
    white-space: nowrap;
    cursor: pointer;
    z-index: 1;
  }
  .mithraCarpooling {
    margin: 0;
    width: 239.3px;
    position: relative;
    font-size: inherit;
    font-weight: 700;
    font-family: inherit;
    background: linear-gradient(90deg, #fb0f72, #fe8d08);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
    flex-shrink: 0;
    z-index: 1;
  }
  .brand {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    margin-top: -37.4px;
    font-size: 21px;
    font-family: var(--font-fahkwang);
  }
  .navigationBar1 {
    align-self: stretch;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    padding: 16px 232.1px 37.2px 101px;
    position: relative;
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
  .aboutUs2 {
    flex: 1;
    position: relative;
    text-decoration: underline;
    z-index: 1;
  }
  .button11 {
    width: 133.9px;
    margin: 0 !important;
    position: absolute;
    top: 16px;
    right: 98.1px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: var(--padding-7xs-6) var(--padding-smi-7) var(--padding-mini-8)
      var(--padding-sm-7);
    box-sizing: border-box;
    white-space: nowrap;
    cursor: pointer;
    z-index: 2;
  }
  .mainView {
    align-self: stretch;
    height: 99.6px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    position: relative;
  }
  .sad1Icon {
    width: 652px;
    position: relative;
    max-height: 100%;
    object-fit: cover;
    max-width: 100%;
  }
  .errorMessagePanel {
    width: 1172px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    padding: 0px var(--padding-xl);
    box-sizing: border-box;
    max-width: 100%;
  }
  .oopsYourProfile {
    margin: 0;
    align-self: stretch;
    position: relative;
    font-size: inherit;
    font-weight: 900;
    font-family: inherit;
  }
  .messageContainer {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 96px;
    max-width: 100%;
  }
  .content {
    width: 1350px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-end;
    padding: 0px 11px 72.6px;
    box-sizing: border-box;
    max-width: 100%;
    text-align: left;
    font-size: 50px;
    color: var(--color-black);
    font-family: var(--font-inter);
  }
  .footer1 {
    align-self: stretch;
    flex: 1;
    position: relative;
    background: linear-gradient(90deg, #fb0f72, #f9a84a);
    max-width: 100%;
  }
  .footer {
    margin-right: -4px;
    align-self: stretch;
    height: 48px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    max-width: 100%;
  }
  .profileNotVerified {
    width: 100%;
    position: relative;
    background-color: #fad3a5;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-start;
    gap: 123.4px;
    line-height: normal;
    letter-spacing: normal;
    text-align: center;
    font-size: var(--font-size-sm);
    color: var(--color-black);
    font-family: var(--font-chenla);
  }

  @media screen and (max-width: 750px) {
    .navigationBar1 {
      padding-left: 50px;
      padding-right: 116px;
      box-sizing: border-box;
    }

    .oopsYourProfile {
      font-size: 40px;
    }

    .profileNotVerified {
      gap: 62px;
    }
  }
  @media screen and (max-width: 675px) {
    .messageContainer {
      gap: 48px;
    }

    .content {
      padding-bottom: 47px;
      box-sizing: border-box;
    }
  }
  @media screen and (max-width: 450px) {
    .navigationBar1 {
      padding-left: var(--padding-xl);
      padding-right: var(--padding-xl);
      box-sizing: border-box;
    }

    .oopsYourProfile {
      font-size: 30px;
    }

    .messageContainer {
      gap: 24px;
    }

    .profileNotVerified {
      gap: 31px;
    }
  }
</style>
