PyTorch 示例
---------------------------------------------
Recipes are bite-sized, actionable examples of how to use specific PyTorch features, different from our full-length tutorials.

与入门教程不同，此系列通过简洁实用的示例，展示了如何使用PyTorch的特性。





.. raw:: html

        </div>
    </div>

    <div id="tutorial-cards-container">

    <nav class="navbar navbar-expand-lg navbar-light tutorials-nav col-12">
        <div class="tutorial-tags-container">
            <div id="dropdown-filter-tags">
                <div class="tutorial-filter-menu">
                    <div class="tutorial-filter filter-btn all-tag-selected" data-tag="all">All</div>
                </div>
            </div>
        </div>
    </nav>

    <hr class="tutorials-hr">

    <div class="row">

    <div id="tutorial-cards">
    <div class="list">

.. Add recipe cards below this line

.. Basics

.. customcarditem::
   :header: PyTorch 加载数据
   :card_description: 学习如何使用 PyTorch 来准备和加载常见的数据集。
   :image: ../_static/img/thumbnails/cropped/loading-data.PNG
   :link: ../recipes/recipes/loading_data_recipe.html
   :tags: Basics


.. customcarditem::
   :header: PyTorch 创建神经网络
   :card_description: 学习如何使用torch.nn，为MNIST数据集创建一个神经网络。
   :image: ../_static/img/thumbnails/cropped/defining-a-network.PNG
   :link: ../recipes/recipes/defining_a_neural_network.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch 中 state_dict 是什么
   :card_description: 学习如何使用 `state_dict` 对象和 Python 字典在 PyTorch 中保存或加载模型。
   :image: ../_static/img/thumbnails/cropped/what-is-a-state-dict.PNG
   :link: ../recipes/recipes/what_is_state_dict.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch 保存和加载模型
   :card_description: 在PyTorch中保存和加载模型用于推理的两种方式 - state_dict和完整模型。
   :image: ../_static/img/thumbnails/cropped/saving-and-loading-models-for-inference.PNG
   :link: ../recipes/recipes/saving_and_loading_models_for_inference.html
   :tags: Basics


.. customcarditem::
   :header: PyTorch 保存和加载通用检查点
   :card_description: 保存和加载一个通用的检查点模型,可以帮助您从上次停止的地方继续推理或训练。在这个示例中,探索如何保存和加载多个检查点。
   :image: ../_static/img/thumbnails/cropped/saving-and-loading-general-checkpoint.PNG
   :link: ../recipes/recipes/saving_and_loading_a_general_checkpoint.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch 在一个文件中保存和加载多个模型
   :card_description: 在这个示例中,学习保存和加载多个模型,有助于重用您之前训练过的模型。
   :image: ../_static/img/thumbnails/cropped/saving-multiple-models.PNG
   :link: ../recipes/recipes/saving_multiple_models_in_one_file.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch 使用不同模型的参数对模型进行热启动
   :card_description: 了解如何通过部分加载模型或加载部分模型方式来热启动训练过程,这可以帮助您的模型比从头开始训练收敛得更快。
   :image: ../_static/img/thumbnails/cropped/warmstarting-models.PNG
   :link: ../recipes/recipes/warmstarting_model_using_parameters_from_a_different_model.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch 跨设备保存和加载模型
   :card_description: 了解如何使用PyTorch在不同设备(CPU和GPU)之间保存和加载模型。
   :image: ../_static/img/thumbnails/cropped/saving-and-loading-models-across-devices.PNG
   :link: ../recipes/recipes/save_load_across_devices.html
   :tags: Basics

.. customcarditem::
   :header:  PyTorch 清零梯度
   :card_description: 了解何时应该清零梯度,以及这样做如何有助于提高模型的精度。
   :image: ../_static/img/thumbnails/cropped/zeroing-out-gradients.PNG
   :link: ../recipes/recipes/zeroing_out_gradients.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch Benchmark
   :card_description: Learn how to use PyTorch's benchmark module to measure and compare the performance of your code
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/recipes/benchmark.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch Benchmark Timer 快速入门
   :card_description: 学习如何测量代码片段的运行时间和收集指令。
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/recipes/timer_quick_start.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch Profiler
   :card_description: 学习如何使用 PyTorch Profiler 来测量算子的时间和内存消耗。
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/recipes/profiler_recipe.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch Profiler with Instrumentation and Tracing Technology API (ITT API) support
   :card_description: Learn how to use PyTorch's profiler with Instrumentation and Tracing Technology API (ITT API) to visualize operators labeling in Intel® VTune™ Profiler GUI
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/profile_with_itt.html
   :tags: Basics

.. customcarditem::
   :header: Torch Compile IPEX Backend
   :card_description: Learn how to use torch.compile IPEX backend
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/torch_compile_backend_ipex.html
   :tags: Basics

.. customcarditem::
   :header: Reasoning about Shapes in PyTorch
   :card_description: Learn how to use the meta device to reason about shapes in your model.
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/recipes/reasoning_about_shapes.html
   :tags: Basics

.. customcarditem::
   :header: Tips for Loading an nn.Module from a Checkpoint
   :card_description: Learn tips for loading an nn.Module from a checkpoint.
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/recipes/module_load_state_dict_tips.html
   :tags: Basics

.. customcarditem::
   :header: (beta) Using TORCH_LOGS to observe torch.compile
   :card_description: Learn how to use the torch logging APIs to observe the compilation process.
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/torch_logs.html
   :tags: Basics

.. customcarditem::
   :header: Extension points in nn.Module for loading state_dict and tensor subclasses
   :card_description: New extension points in nn.Module.
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/recipes/swap_tensors.html
   :tags: Basics


.. Interpretability

.. customcarditem::
   :header: Model Interpretability using Captum
   :card_description: Learn how to use Captum attribute the predictions of an image classifier to their corresponding image features and visualize the attribution results.
   :image: ../_static/img/thumbnails/cropped/model-interpretability-using-captum.png
   :link: ../recipes/recipes/Captum_Recipe.html
   :tags: Interpretability,Captum

.. customcarditem::
   :header: How to use TensorBoard with PyTorch
   :card_description: Learn basic usage of TensorBoard with PyTorch, and how to visualize data in TensorBoard UI
   :image: ../_static/img/thumbnails/tensorboard_scalars.png
   :link: ../recipes/recipes/tensorboard_with_pytorch.html
   :tags: Visualization,TensorBoard

.. Quantization

.. customcarditem::
   :header: Dynamic Quantization
   :card_description:  Apply dynamic quantization to a simple LSTM model.
   :image: ../_static/img/thumbnails/cropped/using-dynamic-post-training-quantization.png
   :link: ../recipes/recipes/dynamic_quantization.html
   :tags: Quantization,Text,Model-Optimization


.. Production Development

.. customcarditem::
   :header: TorchScript for Deployment
   :card_description: Learn how to export your trained model in TorchScript format and how to load your TorchScript model in C++ and do inference.
   :image: ../_static/img/thumbnails/cropped/torchscript_overview.png
   :link: ../recipes/torchscript_inference.html
   :tags: TorchScript

.. customcarditem::
   :header: Deploying with Flask
   :card_description: Learn how to use Flask, a lightweight web server, to quickly setup a web API from your trained PyTorch model.
   :image: ../_static/img/thumbnails/cropped/using-flask-create-restful-api.png
   :link: ../recipes/deployment_with_flask.html
   :tags: Production,TorchScript

.. customcarditem::
   :header: PyTorch Mobile Performance Recipes
   :card_description: List of recipes for performance optimizations for using PyTorch on Mobile (Android and iOS).
   :image: ../_static/img/thumbnails/cropped/mobile.png
   :link: ../recipes/mobile_perf.html
   :tags: Mobile,Model-Optimization

.. customcarditem::
   :header: Making Android Native Application That Uses PyTorch Android Prebuilt Libraries
   :card_description: Learn how to make Android application from the scratch that uses LibTorch C++ API and uses TorchScript model with custom C++ operator.
   :image: ../_static/img/thumbnails/cropped/android.png
   :link: ../recipes/android_native_app_with_custom_op.html
   :tags: Mobile

.. customcarditem::
  :header: Fuse Modules recipe
  :card_description: Learn how to fuse a list of PyTorch modules into a single module to reduce the model size before quantization.
  :image: ../_static/img/thumbnails/cropped/mobile.png
  :link: ../recipes/fuse.html
  :tags: Mobile

.. customcarditem::
  :header: Quantization for Mobile Recipe
  :card_description: Learn how to reduce the model size and make it run faster without losing much on accuracy.
  :image: ../_static/img/thumbnails/cropped/mobile.png
  :link: ../recipes/quantization.html
  :tags: Mobile,Quantization

.. customcarditem::
  :header: Script and Optimize for Mobile
  :card_description: Learn how to convert the model to TorchScipt and (optional) optimize it for mobile apps.
  :image: ../_static/img/thumbnails/cropped/mobile.png
  :link: ../recipes/script_optimized.html
  :tags: Mobile

.. customcarditem::
  :header: Model Preparation for iOS Recipe
  :card_description: Learn how to add the model in an iOS project and use PyTorch pod for iOS.
  :image: ../_static/img/thumbnails/cropped/ios.png
  :link: ../recipes/model_preparation_ios.html
  :tags: Mobile

.. customcarditem::
  :header: Model Preparation for Android Recipe
  :card_description: Learn how to add the model in an Android project and use the PyTorch library for Android.
  :image: ../_static/img/thumbnails/cropped/android.png
  :link: ../recipes/model_preparation_android.html
  :tags: Mobile

.. customcarditem::
   :header: Mobile Interpreter Workflow in Android and iOS
   :card_description: Learn how to use the mobile interpreter on iOS and Andriod devices.
   :image: ../_static/img/thumbnails/cropped/mobile.png
   :link: ../recipes/mobile_interpreter.html
   :tags: Mobile

.. customcarditem::
   :header: Profiling PyTorch RPC-Based Workloads
   :card_description: How to use the PyTorch profiler to profile RPC-based workloads.
   :image: ../_static/img/thumbnails/cropped/profile.png
   :link: ../recipes/distributed_rpc_profiling.html
   :tags: Production

.. Automatic Mixed Precision

.. customcarditem::
   :header: Automatic Mixed Precision
   :card_description: Use torch.cuda.amp to reduce runtime and save memory on NVIDIA GPUs.
   :image: ../_static/img/thumbnails/cropped/amp.png
   :link: ../recipes/recipes/amp_recipe.html
   :tags: Model-Optimization

.. Performance

.. customcarditem::
   :header: Performance Tuning Guide
   :card_description: Tips for achieving optimal performance.
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/recipes/tuning_guide.html
   :tags: Model-Optimization

.. customcarditem::
   :header: PyTorch Inference Performance Tuning on AWS Graviton Processors
   :card_description: Tips for achieving the best inference performance on AWS Graviton CPUs
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/inference_tuning_on_aws_graviton.html
   :tags: Model-Optimization

.. Leverage Advanced Matrix Extensions

.. customcarditem::
   :header: Leverage Intel® Advanced Matrix Extensions
   :card_description: Learn to leverage Intel® Advanced Matrix Extensions.
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/amx.html
   :tags: Model-Optimization

.. (beta) Compiling the Optimizer with torch.compile

.. customcarditem::
   :header: (beta) Compiling the Optimizer with torch.compile
   :card_description: Speed up the optimizer using torch.compile
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/compiling_optimizer.html
   :tags: Model-Optimization

.. (beta) Running the compiled optimizer with an LR Scheduler

.. customcarditem::
   :header: (beta) Running the compiled optimizer with an LR Scheduler
   :card_description: Speed up training with LRScheduler and torch.compiled optimizer
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/compiling_optimizer_lr_scheduler.html
   :tags: Model-Optimization

.. Using User-Defined Triton Kernels with ``torch.compile``

.. customcarditem::
   :header: Using User-Defined Triton Kernels with ``torch.compile``
   :card_description: Learn how to use user-defined kernels with ``torch.compile``
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/torch_compile_user_defined_triton_kernel_tutorial.html
   :tags: Model-Optimization

.. Intel(R) Extension for PyTorch*

.. customcarditem::
   :header: Intel® Extension for PyTorch*
   :card_description: Introduction of Intel® Extension for PyTorch*
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/intel_extension_for_pytorch.html
   :tags: Model-Optimization

.. Intel(R) Neural Compressor for PyTorch*

.. customcarditem::
   :header: Intel® Neural Compressor for PyTorch
   :card_description: Ease-of-use quantization for PyTorch with Intel® Neural Compressor.
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/intel_neural_compressor_for_pytorch.html
   :tags: Quantization,Model-Optimization

.. Distributed Training

.. customcarditem::
   :header: Getting Started with DeviceMesh
   :card_description: Learn how to use DeviceMesh
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/distributed_device_mesh.html
   :tags: Distributed-Training

.. customcarditem::
   :header: Shard Optimizer States with ZeroRedundancyOptimizer
   :card_description: How to use ZeroRedundancyOptimizer to reduce memory consumption.
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/zero_redundancy_optimizer.html
   :tags: Distributed-Training

.. customcarditem::
   :header: Direct Device-to-Device Communication with TensorPipe RPC
   :card_description: How to use RPC with direct GPU-to-GPU communication.
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/cuda_rpc.html
   :tags: Distributed-Training

.. customcarditem::
   :header: Distributed Optimizer with TorchScript support
   :card_description: How to enable TorchScript support for Distributed Optimizer.
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/distributed_optim_torchscript.html
   :tags: Distributed-Training,TorchScript

.. customcarditem::
   :header: Getting Started with Distributed Checkpoint (DCP)
   :card_description: Learn how to checkpoint distributed models with Distributed Checkpoint package.
   :image: ../_static/img/thumbnails/cropped/Getting-Started-with-DCP.png
   :link: ../recipes/distributed_checkpoint_recipe.html
   :tags: Distributed-Training

.. TorchServe

.. customcarditem::
   :header: Deploying a PyTorch Stable Diffusion model as a Vertex AI Endpoint
   :card_description: Learn how to deploy model in Vertex AI with TorchServe
   :image: ../_static/img/thumbnails/cropped/generic-pytorch-logo.png
   :link: ../recipes/torchserve_vertexai_tutorial.html
   :tags: Production

.. End of tutorial card section

.. raw:: html

    </div>

    <div class="pagination d-flex justify-content-center"></div>

    </div>

    </div>

.. -----------------------------------------
.. Page TOC
.. -----------------------------------------
.. toctree::
   :hidden:

   /recipes/recipes/loading_data_recipe
   /recipes/recipes/defining_a_neural_network
   /recipes/torch_logs
   /recipes/recipes/what_is_state_dict
   /recipes/recipes/saving_and_loading_models_for_inference
   /recipes/recipes/saving_and_loading_a_general_checkpoint
   /recipes/recipes/saving_multiple_models_in_one_file
   /recipes/recipes/warmstarting_model_using_parameters_from_a_different_model
   /recipes/recipes/save_load_across_devices
   /recipes/recipes/zeroing_out_gradients
   /recipes/recipes/profiler_recipe
   /recipes/recipes/profile_with_itt
   /recipes/recipes/Captum_Recipe
   /recipes/recipes/tensorboard_with_pytorch
   /recipes/recipes/dynamic_quantization
   /recipes/recipes/amp_recipe
   /recipes/recipes/tuning_guide
   /recipes/recipes/intel_extension_for_pytorch
   /recipes/compiling_optimizer
   /recipes/torch_compile_backend_ipex
   /recipes/torchscript_inference
   /recipes/deployment_with_flask
   /recipes/distributed_rpc_profiling
   /recipes/zero_redundancy_optimizer
   /recipes/cuda_rpc
   /recipes/distributed_optim_torchscript
   /recipes/mobile_interpreter
