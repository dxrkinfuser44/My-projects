import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:fl_chart/fl_chart.dart';

class GraphPage extends StatefulWidget {
  const GraphPage({super.key});

  @override
  _GraphPageState createState() => _GraphPageState();
}

class _GraphPageState extends State<GraphPage> {
  List<FlSpot> dataPoints = [];
  final TextEditingController xController = TextEditingController();
  final TextEditingController yController = TextEditingController();
  bool isLoading = true;
  String? errorMessage;

  // Fetch data from the backend API
  Future<void> fetchData() async {
    setState(() {
      isLoading = true;
      errorMessage = null;
    });

    try {
      final response = await http.get(Uri.parse('http://127.0.0.1:5000/api/data'));
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        setState(() {
          dataPoints = List<FlSpot>.generate(
            data['x'].length,
            (index) => FlSpot(
              data['x'][index].toDouble(),
              data['y'][index].toDouble(),
            ),
          );
          isLoading = false;
        });
      } else {
        setState(() {
          errorMessage = 'Failed to load data';
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = 'Failed to load data: $e';
        isLoading = false;
      });
    }
  }

  // Function to send data to backend API
  Future<void> addDataPoint(double x, double y) async {
    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:5000/api/add_data'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'x': x, 'y': y}),
      );

      if (response.statusCode == 200) {
        fetchData(); // Refresh the graph after adding data
        xController.clear();
        yController.clear();
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Failed to add data')),
        );
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Failed to add data: $e')),
      );
    }
  }

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Graph Page")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            // Form for data input
            Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: xController,
                    decoration: InputDecoration(
                      labelText: 'X Value',
                      border: OutlineInputBorder(),
                    ),
                    keyboardType: TextInputType.number,
                  ),
                ),
                SizedBox(width: 10),
                Expanded(
                  child: TextField(
                    controller: yController,
                    decoration: InputDecoration(
                      labelText: 'Y Value',
                      border: OutlineInputBorder(),
                    ),
                    keyboardType: TextInputType.number,
                  ),
                ),
                IconButton(
                  icon: Icon(Icons.add),
                  onPressed: () {
                    final x = double.tryParse(xController.text);
                    final y = double.tryParse(yController.text);
                    if (x != null && y != null) {
                      addDataPoint(x, y);
                    } else {
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text('Please enter valid numbers')),
                      );
                    }
                  },
                ),
              ],
            ),
            SizedBox(height: 20),
            // Display the graph
            Expanded(
              child: isLoading
                  ? Center(child: CircularProgressIndicator())
                  : errorMessage != null
                      ? Center(child: Text(errorMessage!))
                      : LineChart(
                          LineChartData(
                            lineBarsData: [
                              LineChartBarData(
                                spots: dataPoints,
                                isCurved: true,
                                colors: [Colors.blue],
                                barWidth: 3,
                              ),
                            ],
                          ),
                        ),
            ),
          ],
        ),
      ),
    );
  }
}