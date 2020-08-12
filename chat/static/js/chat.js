function post_message() {
    $.ajax({
        type: 'POST',
        url: '/post_message',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            room_id: '{{ room.id }}',
            message: $.trim($('#message').val()),
        },
        success: function () {
            $('#message').val('');
            get_posts();
            let posts = $("#posts");
            posts.scrollTop(posts.prop("scrollHeight"));
        }
    });
}

function get_posts() {
    $.ajax({
        type: 'POST',
        url: '/get_posts',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            room_id: '{{ room.id }}',
        },
        success: function (data) {
            let posts = $("#posts");
            posts.html('');
            data.reverse().forEach(function (post) {
                posts.append(`
                <div class="media msg">
                    <div class="media-body">
                        <small class="pull-right time"><i class="fa fa-calendar"></i>  ${post.created_date} - <i class="fa fa-clock-o"></i> ${post.created_time}</small>
                        <h5 class="media-heading">${post.author}</h5>
                        <small class="col">${post.message}</small>
                    </div>
                </div>`);
            });
        }
    });
}

function onTextChange() {
    let key = window.event.keyCode;
    if (key === 13) {
        post_message();
        return false;
    }
    else {
        return true;
    }
}