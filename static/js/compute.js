function msToTime(s, output='hours') {
    var ms = s % 1000;
    s = (s - ms) / 1000;
    var secs = s % 60;
    s = (s - secs) / 60;
    var mins = s % 60;
    var hrs = (s - mins) / 60;

    if (output === 'hours') {
        return hrs;
    } else {
        return mins;
    }
}

function get_diff(actualtimeIn, staticTimeBasis, output='hours') {
    // Create date format.
    let logTime = new Date(actualtimeIn);
    let staticTime = new Date(staticTimeBasis);
    // Subtract.
    let difference = logTime - staticTime;
    let time = msToTime(difference, output);

    return time;
}