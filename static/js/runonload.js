async function getroomno() {
   
    fetch(`/details/room`)
        .then(function (response) {
            return response.json();
        }).then(function (all_message) {
            new_length = all_message.length

            
            
            let out_pos = "<option selected>Choose Room No</option>"
           
            
            for (let data of all_message) {
            out_pos+= `<option value="${data.room_no}">${data.room_no}</option>`
            }

            let stock_cards = document.getElementById("roomid")

            stock_cards.innerHTML = out_pos;
            
            //stock_cards.scrollTop = stock_cards.scrollHeight;

        }
    )}

    async function getcourse() {
        
        fetch(`/details/coursename`)
            .then(function (response) {
                return response.json();
            }).then(function (all_message) {
                new_length = all_message.length
    
                
                
                let out_pos = "<option selected>Choose Course</option>"
               
                
                for (let data of all_message) {
                out_pos+= `<option value="${data.course}">${data.course}</option>`
                }
    
                let stock_cards = document.getElementById("courseid")
    
                stock_cards.innerHTML = out_pos;
                
                //stock_cards.scrollTop = stock_cards.scrollHeight;
    
            }
        )}
    
        async function getsection(documentid) {
            let coursename = document.getElementById(documentid).value
    fetch(`/details/course/${coursename}`)
                .then(function (response) {
                    return response.json();
                }).then(function (all_message) {
                    new_length = all_message.length
        
                    
                    
                    let out_pos = "<option selected>Choose Section</option>"
                   
                    
                    for (let data of all_message) {
                    out_pos+= `<option value="${data.section}">${data.section}</option>`
                    }
        
                    let stock_cards = document.getElementById("sectionid")
        
                    stock_cards.innerHTML = out_pos;
                    
                    //stock_cards.scrollTop = stock_cards.scrollHeight;
        
                }
            )}

            async function getsemester(documentid) {
                let coursename = document.getElementById(documentid).value
        fetch(`/details/semester/${coursename}`)
                    .then(function (response) {
                        return response.json();
                    }).then(function (all_message) {
                        new_length = all_message.length
            
                        
                        
                        let out_pos = "<option selected>Choose Semester</option>"
                       
                        
                        for (let data of all_message) {
                        out_pos+= `<option value="${data.semester}">${data.semester}</option>`
                        }
            
                        let stock_cards = document.getElementById("semesterid")
            
                        stock_cards.innerHTML = out_pos;
                        
                        //stock_cards.scrollTop = stock_cards.scrollHeight;
            
                    }
                )}
                async function getsubjectcode() {

            fetch(`/details/subject`)
                        .then(function (response) {
                            return response.json();
                        }).then(function (all_message) {
                            new_length = all_message.length
                
                            
                            
                            let out_pos = "<option selected>Choose Subject code</option>"
                           
                            
                            for (let data of all_message) {
                            out_pos+= `<option value="${data.subjectcode}">${data.subjectcode}</option>`
                            }
                
                            let stock_cards = document.getElementById("subjectcodeid")
                
                            stock_cards.innerHTML = out_pos;
                            
                            //stock_cards.scrollTop = stock_cards.scrollHeight;
                
                        }
                    )}


                    async function selectedsubjectname(documentid) {
                        let subjectcode = document.getElementById(documentid).value 
                        fetch(`/details/subject`)
                        .then(function (response) {
                            return response.json();
                        }).then(function (all_message) {
                            new_length = all_message.length
                
                            let out_pos = ""
                            for (let data of all_message) {
                                // console.log(data.subjectcode)
                                if (data.subjectcode == subjectcode)
                                {
                                    out_pos += `<input class="form-control form-livedoc-control" id="subjectid" type="text" placeholder="Year" value = "${data.name}" readonly/>`
                                }
                        
                            }
                
                            let stock_cards = document.getElementById("subjectnameid")
                
                            stock_cards.innerHTML = out_pos;
                            
                            //stock_cards.scrollTop = stock_cards.scrollHeight;
                
                        }
                    )}


                    async function getfacultycode() {

                        fetch(`/details/faculty`)
                                    .then(function (response) {
                                        return response.json();
                                    }).then(function (all_message) {
                                        new_length = all_message.length
                            
                                        
                                        
                                        let out_pos = "<option selected>Choose Faculty Reg No</option>"
                                       
                                        
                                        for (let data of all_message) {
                                        out_pos+= `<option value="${data.regno}">${data.regno}</option>`
                                        }
                            
                                        let stock_cards = document.getElementById("facultycodeid")
                            
                                        stock_cards.innerHTML = out_pos;
                                        
                                        //stock_cards.scrollTop = stock_cards.scrollHeight;
                            
                                    }
                                )}
            
            
                                async function selectedfacultyname(documentid) {
                                    let regno = document.getElementById(documentid).value 
                                    fetch(`/details/faculty`)
                                    .then(function (response) {
                                        return response.json();
                                    }).then(function (all_message) {
                                        new_length = all_message.length
                            
                                        let out_pos = ""
                                        for (let data of all_message) {
                                            // console.log(data.subjectcode)
                                            if (data.regno == regno)
                                            {
                                                out_pos += `<input class="form-control form-livedoc-control" id="facultyid" type="text" placeholder="Year" value = "${data.name}" readonly/>`
                                            }
                                    
                                        }
                            
                                        let stock_cards = document.getElementById("facultynameid")
                            
                                        stock_cards.innerHTML = out_pos;
                                        
                                        //stock_cards.scrollTop = stock_cards.scrollHeight;
                            
                                    }
                                )}
                                async function gettimeslot() {
                                    
                                    fetch(`/details/timeslot`)
                                        .then(function (response) {
                                            return response.json();
                                        }).then(function (all_message) {
                                            new_length = all_message.length
                                
                                            
                                            
                                            let out_pos = "<option selected>Choose Timeslot</option>"
                                           
                                            
                                            for (let data of all_message) {
                                            out_pos+= `<option value="${data.timeslot}">${data.timeslot}</option>`
                                            }
                                
                                            let stock_cards = document.getElementById("timeslotid")
                                
                                            stock_cards.innerHTML = out_pos;
                                            
                                            //stock_cards.scrollTop = stock_cards.scrollHeight;
                                
                                        }
                                    )}


                                    async function getcurrentdate() {
                                        const dateInput = document.getElementById('doaid');

                                        // ✅ Using the visitor's timezone
                                        dateInput.value = formatDate();
                                        
                                        console.log(formatDate());
                                        
                                        function padTo2Digits(num) {
                                          return num.toString().padStart(2, '0');
                                        }
                                        
                                        function formatDate(date = new Date()) {
                                          return [
                                            date.getFullYear(),
                                            padTo2Digits(date.getMonth() + 1),
                                            padTo2Digits(date.getDate()),
                                          ].join('-');
                                        }
                                        
                                      
                                    }
                                    async function getupdatestudentdetails(documentid) {
                                        let admo = document.getElementById(documentid).value 
                                        fetch(`/details/student/${admo}`)
                                            .then(function (response) {
                                                return response.json();
                                            }).then(function (all_message) {
                                                console.log(all_message)
                                                // new_length = all_message.length
                                                let out_pos =""
                                    
                                                for (let data of all_message) {
                                                    
                                                    console.log(data)
                                                
                                                 out_pos += `
                                                
                                                <div class="col-md-6">
                    <label class="visually-hidden" for="inputSection">Section</label>
                    <input class="form-control form-livedoc-control" id="admissionnoid" type="text" placeholder="Admission No." name = 'admissionno' value = '${data.admission_no}' />
                </div>
                <div class="col-6">
                    <div class="d-grid">
                      <a class="btn btn-primary rounded-pill" onclick = "getupdatestudentdetails('admissionnoid')">Find</a>
                    </div>
                </div>
                <div class="col-md-6">
                  <label class="visually-hidden" for="inputSection">Section</label>
                  <input class="form-control form-livedoc-control" id="inputSection" type="text" placeholder="Enrollment No." name = 'enrollmentno' value = '${data.enrollment_no}' />
              </div>

              <div class="col-md-6">
                <label class="visually-hidden" for="inputSection">Section</label>
                <input class="form-control form-livedoc-control" id="inputSection" type="text" placeholder="Name" name = 'studentname' value = '${data.name}' />
            </div>

            <div class="col-md-6">
              <label class="visually-hidden" for="inputTeacher">Date Of Birth:</label>
              <input class="form-control form-livedoc-control" id="inputTeacher" type="date" placeholder="Date of Birth" name = 'dob' value = '${data.dob}' />
            </div>

            <div class="col-md-6">
              <label for="inputCourse" class="form-label visually-hidden">Gender:</label>
              <select class="form-select form-livedoc-control" id="inputCourse" name = 'gender' value = '${data.gender}'>
                  <option selected value = '${data.gender}' >${data.gender}</option>
              </select>

          </div>

          <div class="col-md-6">
            <label for="inputCourse" class="form-label visually-hidden">course</label>
            <select class="form-select form-livedoc-control" id="courseid" name = 'course' value = '${data.course}'>
            <option value = '${data.course}' selected>${data.course}</option>

            </select>
          </div>


          <div class="col-md-6">
            <label for="inputCourse" class="form-label visually-hidden"><section></section></label>
            <select class="form-select form-livedoc-control" name = 'semester' value = '${data.semester}' id="semesterid">
                <option value = '${data.semester}' selected>${data.semester}</option>

            </select>
          </div>


          <div class="col-md-6">
            <label for="inputCourse" class="form-label visually-hidden"><section></section></label>
            <select class="form-select form-livedoc-control" name = 'section' value = '${data.section}' id="sectionid">
            <option value = '${data.section}' selected>${data.section}</option>

            </select>
          </div>

                <div class="col-md-6">
                  <label class="visually-hidden" for="inputTeacher">Mobile No:</label>
                  <input class="form-control form-livedoc-control" id="inputTeacher" type="number" value = '${data.mob}' name = "mobile" placeholder="Mobile No" />
                </div>
                <div class="col-md-6">
                  <label class="visually-hidden" for="inputTeacher">Email ID:</label>
                  <input class="form-control form-livedoc-control" id="inputTeacher" type="text" name = "email" value = '${data.email}'  placeholder="Email Id" />
                </div>
              
                                                
                                                `
                                                }
                                                
                                                // for (let data of all_message) {
                                                // out_pos+= `<option value="${data.timeslot}">${data.timeslot}</option>`
                                                // }
                                    
                                                let stock_cards = document.getElementById("fullformudpatedata")
                                    
                                                stock_cards.innerHTML = out_pos;
                                                
                                                stock_cards.scrollTop = stock_cards.scrollHeight;
                                    
                                            }
                                        )}

                                    async function sendtoupdate(roomid, courseid, sectionid,semesterid, subjectid,facultycodeid, timeslotid,doaid) {
                                        let room = document.getElementById(roomid).value
                                    let course = document.getElementById(courseid).value  
                                    let section = document.getElementById(sectionid).value 
                                    let semester = document.getElementById(semesterid).value
                                    let subject = document.getElementById(subjectid).value 
                                    let faculty = document.getElementById(facultycodeid).value 
                                    let timeslot = document.getElementById(timeslotid).value
                                    let doa = document.getElementById(doaid).value

                                    if (room == "Choose Room No"){
                                        room = 'None'
                                    }
                                    if (section == "Choose Section"){
                                        section = 'None'
                                    }
                                    if (semester == "Choose Semester"){
                                        semester = 'None'
                                    }
                                    if (course == "Choose Course"){
                                        course = 'None'
                                    }
                                    if (faculty == "Choose Faculty Reg No"){
                                        faculty = 'None'
                                    }
                                    if (subject == "Choose Subject code"){
                                        subject = 'None'
                                    }
                                    if (timeslot == "Choose Timeslot"){
                                        timeslot = 'None'
                                    }
                             
                                    console.log(room)
                                    console.log(course)
                                    console.log(section)
                                    console.log(semester)
                                    console.log(subject)
                                    console.log(faculty)
                                    console.log(doa)
                                    console.log(timeslot)
   
                                        fetch(`/details/updateapi/${room}/${course}/${section}/${semester}/${subject}/${faculty}/${doa}/${timeslot}`)
                                            .then(function (response) {
                                                return response.json();
                                            }).then(function (all_message) {
                                                new_length = all_message.length
                                                console.log(all_message)
                                    
                                                
                                                let out_pos = ` <table class="table">
                                                <thead>
                                                <tr>
                                                    <th>Room No</th>
                                                    <th>Course</th>
                                                    <th>Section</th>
                                                    <th>Semester</th>
                                                    <th>Subject Code</th>
                                                    <th>Faculty Code</th>
                                                    <th>Date of Attendance</th>
                                                    <th>Timeslot</th>
                                                    <th>Update</th>
                                                    <th>Download</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                `

                                                for (let data of all_message) {
                                                    out_pos+= `
                                                    <tr>
                                                    <td>${data.room}</td>
                                                    <td>${data.course}</td>
                                                    <td>${data.section}</td>
                                                    <td>${data.semester}</td>
                                                    <td>${data.subjectcode}</td>
                                                    <td>${data.facultycode}</td>
                                                    <td>${data.doa}</td>
                                                    <td>${data.timeslot}</td>
                                                    <td><a href ="/attendance/update/${data.id}" class="btn btn-primary rounded-pill btn-xs">UPDATE</a></td>
                                                    <td><a href ="/attendance/download/${data.id}" class="btn btn-primary rounded-pill btn-xs">DOWNLOAD</a></td>
                                                    </tr>
                                                    `
                                                    }
                                                out_pos+= `</tbody>
                                                            </table>`

                                                let stock_cards = document.getElementById("apitableupdate");

                                                stock_cards.innerHTML = out_pos;
                                                
                                                // let out_pos = "<option selected>Choose Room No</option>"
                                               
                                                
                                                // for (let data of all_message) {
                                                // out_pos+= `<option value="${data.room_no}">${data.room_no}</option>`
                                                // }
                                    
                                                // let stock_cards = document.getElementById("roomid")
                                    
                                                // stock_cards.innerHTML = out_pos;
                                                
                                                //stock_cards.scrollTop = stock_cards.scrollHeight;
                                    
                                            }
                                        )}
                                    