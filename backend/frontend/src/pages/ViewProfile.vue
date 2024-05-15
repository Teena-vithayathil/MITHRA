<template>
  <div id="SignUpPage" style="background-color:  #fad3a5; display: flex; flex-direction: column; height: 150vh; text-align: center;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
        <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
        <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
        <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
      </div>
    </header>
    <div v-if="driver" style="background-color:  #fad3a5; display: inline-block; margin-top: 20px;">
      <div>
        <img :src="driver.profilePicture" alt="Profile Picture" class="profile-picture">
        <h3>{{ driver.name }}</h3>
        <p>Age: {{ driver.age }}</p>
        <p>Occupation: {{ driver.occupation }}</p>
        <p>Phone Number: {{ driver.phoneNumber }}</p>
        <p>Rating: {{ driver.rating }}</p>
        <!-- Display star rating -->
        <div class="star-rating">
          <span v-for="n in 5" :key="n" @click="setRating(n)" :class="{ filled: n <= driver.rating }">&#9733;</span>
        </div>
        <p>Reviews:</p>
        <ul style="list-style-type: none;">
          <li v-for="(review, index) in driver.reviews" :key="index">{{ review }}</li>
        </ul>
      </div>
      <div>
        <h3>Leave a Review</h3>
        <textarea v-model="newReview" rows="4" cols="50"></textarea>
        <!-- Display star rating input for new review -->
        <div class="star-rating">
          <span v-for="n in 5" :key="n" @click="setNewReviewRating(n)" :class="{ filled: n <= newReviewRating }">&#9733;</span>
        </div>
        <button @click="submitReview">Submit Review</button>
      </div>
    </div>
  </div>
  <footer class="footerComponent">
    <p>&copy; 2024 Mithra Carpooling. All rights reserved.</p>
    </footer>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      driver: null,
      newReview: '',
      newReviewRating: 0
    };
  },
  mounted() {
    this.get_data();
  },
  methods: {
    submitReview() {
      axios.post('http://127.0.0.1:8000/review-rating/', { review: this.newReview, rating: this.newReviewRating })
         .then(response => {
          console.log(response.data);
          this.newReview= '';
          this.newReviewRating= 0;
          this.get_data();
         })
      .catch(error => {
           console.error('Error submitting review:', error);
         });
    },
    setRating(rating) {
      // This method is not used for submitting a new review, but it could be used for displaying a user's own rating
      // For example, if a user wants to update their own rating of a driver
    },
    get_data(){
    axios.post("http://127.0.0.1:8000/view-profile/")
       .then(response => {
         this.driver = response.data;
       })
    .catch(error => {
         console.error('Error fetching driver profile:', error);
       });
    },
    setNewReviewRating(rating) {
      // Set the star rating for the new review
      this.newReviewRating = rating;
    },
    aboutUs() {
      this.$router.push({ name: "AboutUs" });
    },
    signOut() {
      this.$router.push({ name: "StPage" });
    },
    goToMyProfile() {
      this.$router.push({ name: "YourProfile" });
    }
  }
};
</script>

<style>
.star-rating {
  font-size: 24px;
}

.profile-picture {
  width: 170px; 
  height: auto; 
}

.star-rating span {
  cursor: pointer;
  color: #ccc;
}

.star-rating span.filled {
  color: orange;
}

.footerComponent {
    background: linear-gradient(90deg, #fb0f72, #f9a84a);
    padding: 20px;
    text-align: center;
    color: white;
  }
  .header-links {
    display: flex;
    align-items: center;
  }
</style>
