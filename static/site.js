const vm = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        apod: {},
        arand: {},
        userFilter: "",
        showRand: true,
        currentUser: {},
        csrf_token: "",
    },

    methods: {
        loadAPOD: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/planetary/apod',
                params: {
                    
                    api_key: `${apikey}`,
                    // date: "2021-07-14"
                    // count: 3
                    date: this.userFilter
                    
                }
            }).then((response) => {
                this.apod = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
            
        },
        loadRand: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/planetary/apod',
                params: {
                    
                    api_key: `${apikey}`,
                    count: 3
                
                }
            }).then((response) => {
                this.arand = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        createApod: function(info) {
            let today = new Date()
            let yyyy = today.getFullYear()
            let mm = today.getMonth() + 1
            let dd = today.getDate()

            if (dd < 10) dd = '0' + dd
            if (mm < 10) mm = '0' + mm

            let date = yyyy + '-' + mm + '-' + dd
            
            
            axios({
                
                method: 'post',
                url: '/apis/apod/',
                headers: {
                    "X-CSRFToken": this.csrf_token
                },
                data: {
                    "author": this.currentUser.id,
                    "date": date,
                    "title": info.title,
                    "url": info.url,
                    "explanation": info.explanation,
                    "media": info.media_type
                }
            })
        },
        loadCurrentUser: function() {
            axios({
                method: 'get',
                url: 'apis/currentuser/'
            }).then(response => this.currentUser = response.data)
        }
    },
    
    created: function() {
        this.loadRand()
        this.loadCurrentUser()
    },
    mounted: function() {
        this.csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})