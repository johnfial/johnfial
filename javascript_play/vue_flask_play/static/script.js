// all you do is have delimiters...

const vm = new Vue({
    el: "#vue_app",
    delimiters: ['[[', ']]'],
    data: {
        nums: [5, 5, 3, 3, 1, 1, 9]
        // alternate method was each 'num' as object, i.e.:
        // {number: 5},
        // {number: 5},
        // . . . 
        // TO-DO PARSEFLOAT TO A INT
    },
    methods: {
        addNum: function() {
            this.nums.push(num)
        }
    },
    computed: {
            calc_average: function(){
                // VERSION FOR RAW NUMBER
                let total = 0
                for (let num of nums){
                    total += parseFloat(num)
                }
            average = total / nums.length
            return average
        //     // VERSION FOR NUMS AS OBJECTS
        //     let total = 0
        //     for (let num of nums){
        //         total += parseFloat(num.number)
        //     }
        // average = total / nums.length
        // return average
        }
    }
})