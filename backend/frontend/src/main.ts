import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import DrivingProof from "./pages/DrivingProof.vue";
import ForgotPassword from "./pages/ForgotPassword.vue";
import StPage from "./pages/StPage.vue";
import SignupPage from "./pages/SignupPage.vue";
import IDproofUploadPage from "./pages/IDproofUploadPage.vue";
import LoginPage from "./pages/LoginPage.vue";
import AboutUs from "./pages/AboutUs.vue";
import HomePage from "./pages/HomePage.vue";
import YourProfile from "./pages/YourProfile.vue";
import CreateCarpoolPage from "./pages/CreateCarpoolPage.vue";
import ProfileNotVerified from "./pages/ProfileNotVerified.vue";
import Payment from "./pages/Payment.vue";
import ViewProfile from "./pages/ViewProfile.vue";
import JoinCarpool from "./pages/JoinCarpool.vue";
import SearchPdtDelivery from "./pages/SearchPdtDelivery.vue";
import RequestTable from "./pages/RequestTable.vue";
import RequestStatus from "./pages/RequestStatus.vue";
import FinalPayment from "./pages/FinalPayment.vue";
import Cancel from "./pages/Cancel.vue";
import AdminPage from "./pages/AdminPage.vue";
import CarpoolsCreated from "./pages/CarpoolsCreated.vue";
import "./global.css";

interface Route {
  path: string;
  name: string;
  component: any;
}

const routes: Route[] = [
  {
    path: "/",
    name: "StPage",
    component: StPage,
  },
  {
    path: "/forget_password",
    name: "ForgotPassword",
    component:ForgotPassword,
  },
  {
    path: "/signup-page",
    name: "SignupPage",
    component: SignupPage,
  },
  {
    path: "/idproof-upload-page",
    name: "IDproofUploadPage",
    component: IDproofUploadPage,
  },
  {
    path: "/login-page",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/about-us",
    name: "AboutUs",
    component: AboutUs,
  },
  {
    path: "/home-page",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/my-profile",
    name: "YourProfile",
    component: YourProfile,
  },
  {
    path: "/create-carpool-page",
    name: "CreateCarpoolPage",
    component: CreateCarpoolPage,
  },
  {
    path: "/ProfileNotVerified",
    name: "ProfileNotVerified",
    component: ProfileNotVerified,
  },
  {
    path: "/payment",
    name: "Payment",
    component: Payment,
  },
  {
    path: "/view-profile",
    name: "ViewProfile",
    component: ViewProfile,
  },
  {
    path: "/join-carpool",
    name: "JoinCarpool",
    component: JoinCarpool,
  },
  {
    path: "/search-pdt-delivery",
    name: "SearchPdtDelivery",
    component: SearchPdtDelivery,
  },
  {
    path: "/requests",
    name: "RequestTable",
    component: RequestTable,
  },
  {
    path: "/search-product-delivery",
    name: "SearchPdtDelivery",
    component: SearchPdtDelivery,
  },
  {
    path: "/request-status",
    name: "RequestStatus",
    component: RequestStatus,
  },
  {
    path: "/FinalPayment",
    name: "FinalPayment",
    component: FinalPayment,
  },
  {
    path: "/cancel",
    name: "Cancel",
    component: Cancel,
  },
  {
    path: "/admin-idproof",
    name: "AdminPage",
    component: AdminPage,
  },
  {
    path: "/admin-carpools-created",
    name: "CarpoolsCreated",
    component: CarpoolsCreated,
  },
  {
    path: "/admin-driving-license-proof",
    name: "DrivingLicense",
    component: DrivingProof,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((toRoute, _, next) => {
  const metaTitle = toRoute?.meta?.title as string;
  const metaDesc = toRoute?.meta?.description as string;

  window.document.title = metaTitle || "Mithra Carpooling";
  if (metaDesc) {
    addMetaTag(metaDesc);
  }
  next();
});

const addMetaTag = (value: string) => {
  const element = document.querySelector(`meta[name='description']`);
  if (element) {
    element.setAttribute("content", value);
  }
};

createApp(App).use(router).mount("#app");

export default router;
