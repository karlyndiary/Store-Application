$(function() {
    //Json data by api call for order table
    $.get(orderListApiUrl, function(response){
        if(response){
            var table = '';
            var totalCost = 0;
            $.each(response, function(index, order){
                totalCost += parseFloat(order.grand_total);
                table += '<tr>' +
                '<td>' + order.date_time + '</td>' +
                '<td>' + order.order_id + '</td>' +
                '<td>' + order.customer_name + '</td>' +
                '<td>Rs ' + order.grand_total.toFixed(2) + '</td></tr>';
            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>Rs '+ totalCost.toFixed(2) +'</b></td></tr>';
            $("table").find('tbody').empty().html(table);
        }
    });
});