/**
 * Created by EBRAHIMI on 3/11/2016.
 */
function countUp1(count) {
    var div_by = 10, speed = Math.round(count / div_by), $display = $('.count1'), run_count = 1, int_speed = 24;

    var int = setInterval(function () {
        if (run_count < div_by) {
            $display.text(speed * run_count);
            run_count++;
        } else if (parseInt($display.text()) < count) {
            var curr_count = parseInt($display.text()) + 1;
            $display.text(curr_count);
        } else {
            clearInterval(int);
        }
    }, int_speed);
}

//countUp({{ questions_num['num'] }});

function countUp2(count) {
    var div_by = 10, speed = Math.round(count / div_by), $display = $('.count2'), run_count = 1, int_speed = 24;

    var int = setInterval(function () {
        if (run_count < div_by) {
            $display.text(speed * run_count);
            run_count++;
        } else if (parseInt($display.text()) < count) {
            var curr_count = parseInt($display.text()) + 1;
            $display.text(curr_count);
        } else {
            clearInterval(int);
        }
    }, int_speed);
}

//countUp2({{ questions_num['num'] }});

function countUp3(count) {
    var div_by = 10, speed = Math.round(count / div_by), $display = $('.count3'), run_count = 1, int_speed = 24;

    var int = setInterval(function () {
        if (run_count < div_by) {
            $display.text(speed * run_count);
            run_count++;
        } else if (parseInt($display.text()) < count) {
            var curr_count = parseInt($display.text()) + 1;
            $display.text(curr_count);
        } else {
            clearInterval(int);
        }
    }, int_speed);
}

//countUp3({{ shop_system['sales'] }});

function countUp4(count) {
    var div_by = 10, speed = Math.round(count / div_by), $display = $('.count4'), run_count = 1, int_speed = 24;

    var int = setInterval(function () {
        if (run_count < div_by) {
            $display.text(speed * run_count);
            run_count++;
        } else if (parseInt($display.text()) < count) {
            var curr_count = parseInt($display.text()) + 1;
            $display.text(curr_count);
        } else {
            clearInterval(int);
        }
    }, int_speed);
}

//countUp4({{ news_num['num'] }});
