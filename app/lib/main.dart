// main.dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Grapher')),
        body: const GraphForm(),
      ),
    );
  }
}

class GraphForm extends StatefulWidget {
  const GraphForm({super.key});

  @override
  _GraphFormState createState() => _GraphFormState();
}

class _GraphFormState extends State<GraphForm> {
  final _formKey = GlobalKey<FormState>();
  final _xController = TextEditingController();
  final _yController = TextEditingController();

  Future<void> _submitData() async {
    final xValues = _xController.text.split(',').map((e) => double.parse(e.trim())).toList();
    final yValues = _yController.text.split(',').map((e) => double.parse(e.trim())).toList();

    final response = await http.post(
      Uri.parse('http://127.0.0.1:5000/plot'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'x_values': xValues,
        'y_values': yValues,
        'title': 'Custom Graph',
        'xlabel': 'X-axis',
        'ylabel': 'Y-axis',
      }),
    );

    if (response.statusCode == 200) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Graph plotted successfully!')));
    } else {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Failed to plot graph.')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Form(
        key: _formKey,
        child: Column(
          children: [
            TextFormField(
              controller: _xController,
              decoration: const InputDecoration(labelText: 'X Values (comma separated)'),
              keyboardType: TextInputType.number,
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter X values';
                }
                return null;
              },
            ),
            TextFormField(
              controller: _yController,
              decoration: const InputDecoration(labelText: 'Y Values (comma separated)'),
              keyboardType: TextInputType.number,
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return 'Please enter Y values';
                }
                return null;
              },
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                if (_formKey.currentState!.validate()) {
                  _submitData();
                }
              },
              child: const Text('Plot Graph'),
            ),
          ],
        ),
      ),
    );
  }
}