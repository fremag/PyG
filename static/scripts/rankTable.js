function CreateRanksTable(id, jsonSrc = "/json/nodes", tableId ="nodeTable", style="display") {
    var mainElement = document.getElementById(id);

    var nodeTable = document.createElement("table");
    nodeTable.setAttribute("id", tableId);
    nodeTable.setAttribute("class", style);
nodeTable.innerHTML = "<thead class='thead-dark'>"
+"        <tr>"
+"            <th>Nodes</th>"
+"            <th>Type</th>"
+"            <th>Rank</th>"
+"        </tr>"
+"        </thead>";

    $(document).ready(function() {
        $.getJSON( jsonSrc, function( json ) {
            $('#'+tableId).DataTable({
                    data: json,
                    pageLength: -1,
                    order: [[ 2, "asc" ], [ 1, "asc" ], [ 0, "asc" ]],
                    columns: [
                        {
                            data: 'name',
                            render: function ( data, type, row ) {
                                return '<a href="'+ row['url']+'">'+data+'</a>';
                            }
                        },
                        {
                            data: 'type',
                            render: function ( data, type, row ) {
                                return '<a href="'+ row['type_url']+'">'+data+'</a>';
                            }
                        },
                        {
                            data: 'rank'
                        }
                    ]
                });
        });
    });

    mainElement.appendChild(nodeTable);
}