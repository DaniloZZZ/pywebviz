# Usages

## Machine learning

### Monitor training live
vis.vars.output = ypred
vis.vars.cost.append(cost)

### Change learning rate live



opt = torch.optim.Adam(params, lr=1)

- A
    vis.vars.lr = LiveValue(lr)

    for i in train_loop:
        -- A1
        opt.param_groups[0]['lr'] = vis.vars.lr.value
        -- A2 
        opt.param_groups[0]['lr'] = vis.vars.lr.data
        -- A3 
        opt.param_groups[0]['lr'] = vis.vars.lr.item
        --
        train(opt)

- B
    
    -- B1
    vis.vars.opt_params = DictModifier( opt.param_groups[0] )
    -- B2
    vis.vars.opt_params = KeyModifier( 'lr', opt.param_groups[0] )
    -- B3
    vis.vars.opt = OptimizerVis( opt )
    --
    my_training_routine(opt, model, ...)


- C 
    class MyMon:
        def vis_get(self, key):
            return {'type':'Slider', 'value':opt.param_groups[0]['lr']}

        def vis_set(self, key, value):
            opt.param_groups[0]['lr'] = value

    vis.vis.vars.opt = MyMon()
    




## Scientific experiments

## Quantum computing

## Live logging
