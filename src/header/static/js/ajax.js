jQuery(document).ready(function($) {
    $('#chatid').click(function(e){
        var messagepart = document.getElementById('message-part');
        var userspart = document.getElementById('users-part');
        messagepart.classList.remove('displaynone')
        userspart.classList.add('displaynone')
    });
    $('#usersid').click(function(e){
        var messagepart = document.getElementById('message-part');
        var userspart = document.getElementById('users-part');
        messagepart.classList.add('displaynone')
        userspart.classList.remove('displaynone')
    });
//    $('#lessoncheck').click(function(e){
//        var value = $(this).val()
//        alert(value)
//    });

    $('#sendchat').click(function(e){
        var content = $('#chatFormControlTextarea2').val()

        document.getElementById('chatFormControlTextarea2').value = '';
        if(content.length < 1){
            return false;
        }else{
            $.ajax({
                url: "chatadd/",
                data: {
                    csrfmiddlewaretoken: csrf,
                    lesson: lesson,
                    content: content
                },
                type: 'post',
                success: function (response) {
//                    alert(response.result);
                },
                error: function(response){
                    alert("Xabar jo'natilmadi");
                }
            });
        }

    });


    csrf = $("input[name=csrfmiddlewaretoken]").val()
    var lessoncheckid = document.getElementById('lessoncheck');
    var lesson = $('#lessoncheck').val()
//    alert(lesson)
    var x = setInterval(function () {

        todaytime = new Date()

        $.ajax({
            url: "lessonstatus/",
            data: {
                csrfmiddlewaretoken: csrf,
                lesson: lesson
            },
            type: 'post',
            success: function (response) {

                $.each(response,function(key,value){
                        var hms = value;   // your input string
                        var a = hms.split(':'); // split it at the colons
                        if(todaytime.getMinutes()-a[1] == 0){
//                            if(todaytime.getSeconds()-a[2] < 12){
                                var status = document.getElementById("st"+key)
                                status.classList.remove("danger-color")
                                status.classList.remove("text-danger")
                                status.classList.add("text-success")
//                            }else{
//                                var status = document.getElementById("st"+key)
//                                status.classList.remove("danger-color")
//                                status.classList.remove("text-success")
//                                status.classList.add("text-danger")
//                            }
                        }else{
                            var status = document.getElementById("st"+key)
                            status.classList.remove("danger-color")
                            status.classList.remove("text-success")
                            status.classList.add("text-danger")
                        }
                })
            },
                error: function(response){
                    alert("Aloqa uzildi!!!");
                }
        });



        $.ajax({
            url: "chat/",
            data: {
                csrfmiddlewaretoken: csrf,
                lesson: lesson
            },
            type: 'post',
            success: function (response) {
//                alert(response.result)
                document.getElementById("chatpart").innerHTML = response.result
            },
                error: function(response){
                    alert("Aloqa uzildi!!!");
                }
        });





    }, 3000);

});