/*calendar*/
var month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
];
var weekday = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
];
var weekdayShort = [
    "sun",
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
    "sat"
];
var monthDirection = 0;
var lastClicked = "";

var DAY = "";
var MONTH = "";
var YEAR = "";


function getNextMonth() {
    console.log("getNextMonth")
    monthDirection++;
    var current;
    var now = new Date();
    if (now.getMonth() == 11) {
        current = new Date(now.getFullYear() + monthDirection, 0, 1);
    } else {
        current = new Date(now.getFullYear(), now.getMonth() + monthDirection, 1);
    }
    initCalender(getMonth(current));
}

function getPrevMonth() {
    console.log("getPrevMonth")

    monthDirection--;
    var current;
    var now = new Date();
    if (now.getMonth() == 11) {
        current = new Date(now.getFullYear() + monthDirection, 0, 1);
    } else {
        current = new Date(now.getFullYear(), now.getMonth() + monthDirection, 1);
    }
    initCalender(getMonth(current));
}
Date.prototype.isSameDateAs = function(pDate) {
    return (
        this.getFullYear() === pDate.getFullYear() &&
        this.getMonth() === pDate.getMonth() &&
        this.getDate() === pDate.getDate()
    );
};

function getMonth(currentDay) {

    var now = new Date();
    var currentMonth = month[currentDay.getMonth()];
    var monthArr = [];
    for (i = 1 - currentDay.getDate(); i < 31; i++) {
        var tomorrow = new Date(currentDay);
        tomorrow.setDate(currentDay.getDate() + i);
        if (currentMonth !== month[tomorrow.getMonth()]) {
            break;
        } else {
            monthArr.push({
                date: {
                    weekday: weekday[tomorrow.getDay()],
                    weekday_short: weekdayShort[tomorrow.getDay()],
                    day: tomorrow.getDate(),
                    month: month[tomorrow.getMonth()],
                    year: tomorrow.getFullYear(),
                    current_day: now.isSameDateAs(tomorrow) ? true : false,
                    date_info: tomorrow
                }
            });
        }
    }
    return monthArr;
}

function clearCalender() {
    console.log("clearCalender")

    $("table tbody tr").each(function() {
        $(this).find("td").removeClass("active selectable currentDay between hover").html("");
    });
    $("td").each(function() {
        $(this).unbind('mouseenter').unbind('mouseleave');
    });
    $("td").each(function() {
        $(this).unbind('click');
    });
    clickCounter = 0;
}

function initCalender(monthData) {
    console.log("initCalender")

    var row = 0;
    var classToAdd = "";
    var currentDay = "";
    var today = new Date();

    clearCalender();
    $.each(monthData,
        function(i, value) {
            var weekday = value.date.weekday_short;
            var day = value.date.day;
            var column = 0;
            var index = i + 1;

            DAY = value.date.day;
            MONTH = ""+(month.indexOf(value.date.month)+1);

            if (MONTH.length == 1) {
                MONTH = "0"+MONTH;
            }
            YEAR = value.date.year;


            
            $(".sideb .header .month").html(value.date.month);
            $(".sideb .header .year").html(value.date.year);
            if (value.date.current_day) {
                currentDay = "currentDay";
                classToAdd = "selectable";
                $(".right-wrapper .header span").html(value.date.weekday);
                $(".right-wrapper .day").html(value.date.day);
                $(".right-wrapper .month").html(value.date.month);
            }
            if (today.getTime() < value.date.date_info.getTime()) {
                classToAdd = "selectable";

            }
            $("tr.weedays th").each(function() {
                var row = $(this);
                if (row.data("weekday") === weekday) {
                    column = row.data("column");
                    return;
                }
            });
            var lol = $($($($("tr.days").get(row)).find("td").get(column)).addClass(classToAdd + " " + currentDay));
            var dayDiv = document.createElement("div");
            dayDiv.className = "day"
            dayDiv.innerHTML = day
            var usedBy = document.createElement("div");
            usedBy.className = "usedBy"
            usedBy.className += ` dayCount_${day}`

            lol.append(dayDiv);
            lol.append(usedBy);
            
            /*console.log(lol)*/
            currentDay = "";
            if (column == 6) {
                row++;
            }
        });
    $("td.selectable").click(function() {
        var day = $(this).find(".day").html();
        var year = $(".year").html();
        var monthInt = month.indexOf($(".month").html()) + 1;
        /*console.log(`${day}.${monthInt}.${year}`)*/
        
        clearLastClicked()
        this.style['background-color'] = "var(--3Col)";
        lastClicked = this;

        /*$(this).style("bacground-color var(--3Col); ");*/
        changeDateSide(day, monthInt)
        /*here to handle click*/

        click(day, monthInt, year)

        /*dateClickHandler($(this));*/
    });
}
initCalender(getMonth(new Date()));


function clearLastClicked(){
    if(lastClicked != ""){
        lastClicked.style['background-color'] = "transparent";
    }
        

}
function changeDateSide(day, monthInt){
    console.log("changeDateSide")
    $("#sideDay").html(day);
    $("#sideMonth").html(month[monthInt-1]);

}
/*var clickCounter = 0;
$(".fa-angle-double-right").click(function() {
    $(".right-wrapper").toggleClass("is-active");
    $(this).toggleClass("is-active");
});
*/
/*function dateClickHandler(elem) {
    console.log("dateClickHandler")


    var day1 = parseInt($(elem).html());
    if (clickCounter === 0) {
        $("td.selectable").each(function() {
            $(this).removeClass("active between hover");
        });
    }
    clickCounter++;
    if (clickCounter === 2) {
        $("td.selectable").each(function() {
            $(this).unbind('mouseenter').unbind('mouseleave');
        });
        clickCounter = 0;
        return;
    }
    $(elem).toggleClass("active");
    $("td.selectable").hover(function() {

        var day2 = parseInt($(this).html());
        $(this).addClass("hover");
        $("td.selectable").each(function() {
            $(this).removeClass("between");

        });
        if (day1 > day2 + 1) {
            $("td.selectable").each(function() {
                var dayBetween = parseInt($(this).html());
                if (dayBetween > day2 && dayBetween < day1) {
                    $(this).addClass("between");
                }
            });
        } else if (day1 < day2 + 1) {
            $("td.selectable").each(function() {
                var dayBetween = parseInt($(this).html());
                if (dayBetween > day1 && dayBetween < day2) {
                    $(this).addClass("between");
                }
            });
        }
    }, function() {
        $(this).removeClass("hover");
    });
}*/

$(".fa-angle-left").click(function() {
    console.log("getPrevMonth")
    clearLastClicked();
    getPrevMonth();
    console.log(YEAR, MONTH, DAY)
    
    $(".main").addClass("is-rotated-left");
    setTimeout(function() {
        $(".main").removeClass("is-rotated-left");
    }, 195);
    setTimeout(function(){
    fetchMonth(YEAR, MONTH, DAY)
    }, 100)
});

$(".fa-angle-right").click(function() {
    console.log("getNextMonth")
    clearLastClicked();
    getNextMonth();
    console.log(YEAR, MONTH, DAY)

    $(".main").addClass("is-rotated-right");
    setTimeout(function() {
        $(".main").removeClass("is-rotated-right");
    }, 195);
    console.log(document.getElementsByClassName(`dayCount_1`))
    
    
        console.log("loop")
        fetchMonth(YEAR, MONTH, DAY)
        
});