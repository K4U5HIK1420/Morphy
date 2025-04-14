🗺️ Morphy Language — Feature Roadmap

✅ Phase 1 — Core Foundations (In Progress / Almost Complete)
Goal	                                Status	          Description
💡 Variable Declaration & Assignment	✅ Done	          var x = 10;
🔢 Arithmetic Expressions	            ✅ Done	          x = 5 + 3 * 2;
🧠 Logical & Relational Operators	    ✅ Done	          if (a > b) {}
🧾 String Support	                    ✅ Done	          print("Hello");
🗂️ Control Flow: if	                  ✅ Done	          if (condition) {}
🔁 Loops: for & while	                ⚡ In Progress	  Custom syntax for looping with init, condition, update.
💻 Multi-Line Input in REPL	          🛠️ Planned	      Allow writing full blocks before execution in interpreter.py.

🚀 Phase 2 — Language Expansion
Goal	                              Priority	          Description
🧵 Loops & Nesting	                ⚡ Immediate	      Allow if inside for and nested loops.
🗃️ Functions / Procedures	          🔥 Must-Have	      Custom function definitions: func greet() {}.
📦 Basic Standard Library	          🔥 Must-Have	      Math, Strings, Date, File I/O.
🧠 Boolean Constants	              🧠 Easy             Fix	true and false tokens for logic clarity.
🧠 Error Handling Improvements	    🚧 Planned	        Graceful handling for runtime & syntax errors.

🌟 Phase 3 — Advanced Features & Power-User Tools
Goal	                                Ambition Level	    Description
🧵 Multithreading / Concurrency	      ⚡ High	            spawn {} syntax for parallel logic execution.
🎮 Game / App Scripting Integration	  ⚡ High	            Allow other projects to embed Morphy as a scripting engine.
🧰 Package Manager / Module Support	  💡 Mid	            Import / export user code modules: import utils;.
💾 File & IO Support	                💡 Mid	            file = open("data.txt");
🧑‍💻 Debugger / Execution Tracing	      💡 Mid	            Trace statements during execution for debugging.
🏃 JIT Compilation	                  💡 Ambitious	      Speed up execution by compiling to bytecode or machine code.

💡 Suggested Development Plan:
  Sprint	    Focus
  Sprint 1	  Finalize loops (for / while) with block execution.
  Sprint 2	  Implement functions & true/false literals.
  Sprint 3	  Build out standard library (Math, Strings, IO).
  Sprint 4	  Introduce multithreading (spawn) and module system.
  Sprint 5	  Work on error handling, scripting integration and debugging tools.
