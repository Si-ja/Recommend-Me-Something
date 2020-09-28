<template>
    <div>
        <!--<h4>Home Page</h4>-->
        <div id="optionsSelection">
            <select v-model="table_selected">
                <option disabled value="">Please select one</option>
                <option v-for="table in tables" v-bind:key="table">
                    {{ table }}
                </option>
            </select>
            <button style="margin-left:15px" @click="getRecommendation">Random Recommendation</button>
        </div>

        <div id="informationSelection">
            <p><b>{{ title }} {{ year }}</b></p>
            <p><img :src="img"></p>
            <p>{{ description }}</p>
        </div>
    </div>    
</template>

<style>
#optionsSelection {
  text-align: center;
  padding: 10px;
}

#informationSelection {
    display: inline-block;
    margin: auto;
    width: 40%;
}
</style>

<script>
//axios will allow for bridging the connection between the frontend and the backend api
import axios from 'axios'
export default {
    data() {
        return {
            tables: null,
            table_selected: '',
            title: '',
            img: '',
            description: '',
            year: '',
        }
    },
    methods: {
        getRecommendation() {
            this.getRandomRecommendation()
        },
        getRandomRecommendation() {
            // Get recommendations on a certain product
            const db_selected = this.table_selected
            const path = `http://localhost:5000/api/` + db_selected + `/random`
            axios.get(path)
            .then(response => {
                this.title = response.data.name
                this.year = '(' + response.data.year + ')'
                this.description = response.data.description
                this.img = response.data.img
            })
            .catch(error => {
                console.log('Couldn\'t fetch the request from ' + path)
            })
        },
    },
    created() {
        // Get information on what tables the database works with
        const path = `http://localhost:5000/api/tables`
        axios
            .get(path)
            .then(response => (this.tables = response.data))
        .catch(error => {
            console.log("Error loading the database and finding a database.")
        })
    },
}
</script>
