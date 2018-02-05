//$(document).ready(function(){
    function validate_date(user_date, now){
        var validate=false;
        user_date_a=user_date.split('-');
        now_a=now.split('-');
        now_date_object={};
        user_date_object={};
        now_date_object.year=parseInt(now_a[0]);
        now_date_object.month=parseInt(now_a[1]);
        now_date_object.day=parseInt(now_a[2]);
        user_date_object.year=parseInt(user_date_a[0]);
        user_date_object.month=parseInt(user_date_a[1]);
        user_date_object.day=parseInt(user_date_a[2]);
        if (user_date_object.year>now_date_object.year){
            validate=true;
            return validate;
        }
        else if(user_date_object.year<now_date_object.year){
            validate=false;
            return validate;
        }
        else if(user_date_object.year==now_date_object.year){
            if (user_date_object.month>now_date_object.month){
                validate=true;
                return validate;
            }
            else if(user_date_object.month<user_date_object.month){
                validate= false;
                return validate;
            }
            else if(user_date_object.month==now_date_object.month){
                if(user_date_object.day>now_date_object.day){
                    validate=true;
                    return validate
                }
                else if(user_date_object.day==now_date_object.day){
                    validate=true;
                    return validate;
                }
                else{
                    validate =false;
                    return validate
                }
            }
        }
    }
//});