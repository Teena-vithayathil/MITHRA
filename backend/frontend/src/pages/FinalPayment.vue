<template>
  <div class="payment-container">
    <h1 class="payment">Payment</h1>
    <!-- Main picture in the middle -->
    <img :src="mainPicture" alt="Main Picture" class="main-picture">
    
    <!-- Four small pictures at the bottom -->
    <div class="small-pictures">
      <img v-for="(link, index) in smallPictures" :src="link" :key="index" @click="redirectToWebsite(index)" class="small-picture" style="cursor: pointer;">
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      mainPicture: '', // Path to the main picture passed by Django
      smallPictures: [ // Paths to the small pictures
        '/rectangle-55@2x.png',
        '/rectangle-53@2x.png',
        '/rectangle-54@2x.png',
        '/rectangle-52@2x.png'
      ],
      websites: [ // Corresponding websites for small pictures
        'https://udyogini.org/',
        'https://dashboard.kerala.gov.in/e-services/service.php?fcgzGljlql',
        'https://wcd.nic.in/bbbp-schemes',
        'https://web.umang.gov.in/landing/department/pmmvy.html'
      ]
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/final-payment/')
    .then(response => {
      this.mainPicture = response.data.mainPicture;
    })
    .catch(error => {
      console.error('Error fetching main picture:', error);
    });
},
  methods: {
    redirectToWebsite(index) {
      window.open(this.websites[index], '_blank');
    },
  }
};
</script>

<style>
.payment-container {
  --color-navajowhite: #fad3a5;
  background-color: var(--color-navajowhite);
  padding: 20px;
}

.payment {
  text-align: center;
  font-size: 40px;
}
.main-picture {
  display: block;
  margin: 0 auto;
  width: 400px;
}

.small-pictures {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.small-picture {
  width: 250px;
  height: 200px;
  margin: 0 10px;
}
</style>
