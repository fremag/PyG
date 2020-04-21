function CreateNodeTable(id, tableId ="nodeTable", style="display") {
    var mainElement = document.getElementById(id);

    var nodeTable = document.createElement("table");
    nodeTable.setAttribute("id", tableId);
    nodeTable.setAttribute("class", style);
nodeTable.innerHTML = "<thead class=\"thead-dark\">"
+"        <tr>"
+"            <th>Nodes</th>"
+"            <th>Type</th>"
+"        </tr>"
+"        </thead>"
+"        <tbody>"
+"       </tbody>";

    $(document).ready(function() {
        $.getJSON( "/json/nodes", function( json ) {
            $('#'+tableId).DataTable({
                    data: json,
                    pageLength: -1,
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
                        }
                    ]
                });
        });
    });

    mainElement.appendChild(nodeTable);
}