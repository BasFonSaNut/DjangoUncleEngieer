console.log('hello world quiz')
const url = window.location.href

const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')


const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Time over')
                sendData()
            }, 500)
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        let qrun = 1
        const data = response.data
        // console.log(data.length)
       for(i = 0; i<data.length;i++)
       {
           /*===========QUESTION PART============*/
            for (const [question, value] of Object.entries(data[i])) {
            qid = value['qid'] 
            quizBox.innerHTML += `
                 <hr>
                 <div class="column">
                 <div class="mb-2">
                 <span>สุ่มได้โจทย์ ID :  ${qid}</span>
                 `
            if(value['pic_question'] !==''){
                qpicture = value['pic_question']   
                quizBox.innerHTML += `    
                    <img src="/media/${qpicture}" width="20%">
                    `    
            }
                             
            quizBox.innerHTML += `                 
                 <h5><b>${qrun++}.)  ${question}</b></h5>
                 </div>          
                 `    
            /*===========ANSWER PART============*/
            for (const [keya, valuea] of Object.entries(value['answer2'])) {
               // console.log(`${keya}: ${valuea['ans_id']}`);
                ans_id = valuea['ans_id']
                ans_text = valuea['ans_text']
                q_text = valuea['q_text']
                
                quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" id="${q_text}-${ans_text}" name="${q_text}" value="${ans_text}">
                        <label for="${q_text}">${ans_text}</label>
                    </div>
                        `
            }
           

        }
    }            
       
        activateTimer(response.time)
        
    },
    error: function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            const results = response.results
            console.log(results)
            quizForm.classList.add('not-visible') 

            scoreBox.innerHTML = `${response.passed ? '<font color="green"><h1><b>$$$$...Congratulations...สุดยอด </b></h1></font>' : '<font color="red"><h1><b>!!!...ไม่ผ่านการทดสอบ...สู้ๆ</b></h1></font>'}<h3>Your result is ${response.score.toFixed(2)}% </h3><hr>`
            // scoreBox.classList.add(...cls) 
            // ถ้าใส่คำตอบจะไม่ออกมีแต่คะแนนผ่าน
            let q2run = 1
            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){
                    // questiontxt = resp['text'] 
                    // console.log(questiontext)
                    resDiv.innerHTML += ` <h5><br>${q2run++}. ${question}</h5>`
                    // resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h5']
                    resDiv.classList.add(...cls)

                    if (resp=='not answered') {
                        resDiv.innerHTML += '<h5><br><u>คุณไม่ได้เลือกคำตอบ</u></h5>'
                        resDiv.classList.add('bg-secondary')
                    }
                    else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += `<h5><br><u>ถูกต้อง  :  ${answer}</u></h5>`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` <h5><br><u>คุณตอบผิด  :  ${answer}</u></h5>`
                            resDiv.innerHTML += ` <h5><br><u>คำตอบคือ  :  ${correct}</u></h5>`
                            const ans_des = resp['ansdesc']
                            const answerpic = resp['answerpic']
                            
                            if(answerpic !="" && answerpic != "None"){
                                resDiv.innerHTML += `    
                                <br> <img src="/media/${answerpic}" width="20%">
                                `   
                            }                            
                            if(ans_des!="" && ans_des != "None"){
                                resDiv.innerHTML += ` 
                                <br><span>คำอธิบาย : ${ans_des}</span>
                                `   
                            }    
                        }
                    }
                }
                resultBox.append(resDiv)
                
            })
            resultBox.innerHTML += '<br><center><h5>#############หมายเหตุ กดSaveเพียงครั้งเดียว กดหลายครั้งคะแนนเข้าระบบหลายครั้ง(เอาคะแนนครั้งแรกสุด)#############<hr></h5></center><br>'
            
        },
        error: function(error){
            console.log(error)
        }
        
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})